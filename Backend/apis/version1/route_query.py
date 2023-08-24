from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from chromadb.config import Settings
import chromadb

router = APIRouter()


@router.get("/query={query}")
def query(query: str, db: Session = Depends(get_db)):
    chat = ChatOpenAI(openai_api_key="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"
                      , model="gpt-3.5-turbo-0613")
    messages = [HumanMessage(content= query)]
    ans = chat(messages).content

    return ans

def ask(api,query,query1,query2,c,model,bot_id):
    client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="backend/docs"))  
    collection = client.get_or_create_collection("col" + str(bot_id))
    res = collection.query(query_texts=[query] ,n_results=2)
    model = model.split("-")[1]
    chat = ChatOpenAI(temperature=c,openai_api_key=api['openai'], model="gpt-3.5-turbo-0613")
    context = ". ".join(res["documents"][0])
    messages = [HumanMessage(content=query1 + context + query2)]
    ans = chat(messages).content
    print(ans)
    return ans  

def add_doc(docs, personal_id ,bot_id):
    char_bot_id = "col"+str(bot_id)
    client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="backend/docs" ))
            
    collection = client.get_or_create_collection(char_bot_id) 
    
    ids = list(range(personal_id, personal_id+len(docs)))
    charid = ["id"+str(i) for i in ids]
    collection.add(documents=docs,ids=charid)
    personal_id = personal_id+len(docs)
   
    print(char_bot_id)
    print(collection.count())
    client.persist()
    
    return personal_id
