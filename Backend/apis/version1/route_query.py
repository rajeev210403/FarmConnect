from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from chromadb.config import Settings
import chromadb
from typing import List

from langchain.document_loaders import SeleniumURLLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import SitemapLoader

router = APIRouter()


@router.get("/query={query}")
def query(query: str, db: Session = Depends(get_db)):
    client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="backend/docs"))  
    collection = client.get_or_create_collection("data")
    res = collection.query(query_texts=[query] ,n_results=2)    
    chat = ChatOpenAI(openai_api_key="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"
                      , model="gpt-3.5-turbo-0613")
    messages = [HumanMessage(content= "context : " + res + " question : " + query)]
    ans = chat(messages).content

    return ans
    
def add_doc(docs, index_num ):
    client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="backend/docs" ))
    collection = client.get_or_create_collection("data") 
    ids = list(range(index_num, index_num+len(docs)))
    charid = ["data" + str(i) for i in ids]
    collection.add(documents=docs,ids=charid)
    index_num = index_num+len(docs)
   
    print(collection.count())
    client.persist()
    
    return index_num

@router.post("/urlmethod/")
def train_urls(urls: List[str] ,index_num: int):
    loaders = SeleniumURLLoader(urls=urls)
    data = loaders.load()
    text_splitter = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(data)
    for i in docs:
        add_doc([i.page_content], index_num)
    return "Done"

@router.post("/textmethod/")
def train_text(text: str ,index_num: int): 
    add_doc([text], index_num)
    return "Done"

@router.post("/sitemapmethod/")
def train_sitemap(sitemap: str ,index_num: int): 
    sitemap_loader = SitemapLoader(web_path=sitemap)
    sitemap_loader.requests_kwargs = {"verify": False}
    docs = sitemap_loader.load()
    for i in docs:
        add_doc([i.page_content], index_num)
    return "Done"

@router.post("/pdfmethod/")
def train_pdf(pdfurl: str ,index_num: int): 
    loader = PyPDFLoader(pdfurl)
    pages = loader.load_and_split()
    for i in pages:
        add_doc([i.page_content], index_num)
    return "Done"
