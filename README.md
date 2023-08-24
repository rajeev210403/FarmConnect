# 👨‍🌾FarmConnect
Connecting to farmers: Not just another farming assistant

Revolutionizing agriculture support through unprecedented abstraction, user-friendly interfaces, and ubiquitous access.

## Problem Statement

Designing innovative Android applications to address societal challenges in the Indian context, particularly aligned with the United Nations' Sustainable Development Goals (SDGs), is a formidable yet rewarding endeavor. With India's vast population, cultural diversity, and multilingual landscape, the potential to create meaningful and impactful solutions is immense


## Features

- Multilingual : The app is multilingual, understanding and responding to all the popular regional languages even in hinglish or regional languages written in roman scripts.
![Alt text](image-1.png)
- Semantic Search : Semantic search seeks to improve search accuracy by understanding the searcher's intent and the contextual meaning of terms as they appear in the searchable dataspace, whether on the Web or within a closed system, to generate more relevant results.
- Vector Embeddings: Vector embeddings are a type of data representation that carries within it semantic information that’s critical for the AI to gain understanding and maintain a long-term memory they can draw upon when executing complex tasks.
![Alt text](image-2.png)
- Vector Databases: Vector databases like ChromaDB (opensource) or Pinecone offers optimized storage and querying capabilities for embeddings.
We made our app adaptable , where new information, govt schemes, techniques etc. can be easily fed to the chatbot in the form of PDF , text , html etc. within minutes.
![Alt text](fc1.png)

- **Frontend**: Java
- **Backend**: 
- **IDE**: VS Code, Android Studio
- **Design**: Figma, Canva
- **API Testing & Documentation**: 
- **Version Control**: Git and GitHub

#### GitHub Repository Structure


| S.No. | Branch Name                                                                  | Purpose                       |
| ----- | ---------------------------------------------------------------------------- | ----------------------------- |
| 1.    | [frontend](https://github.com/rudrakshi99/Farmer-Call-Center/tree/master)      | contains all Frontend code    |
| 2.    | [backend](https://github.com/rudrakshi99/Farmer-Call-Center/tree/backend)    | contains all Backend code     |


## 🌾Deployment and Usage
### Deploying the API endpoints (backend)
- Backend is developed using FastAPI (python)
- Go to the backend folder 
```bash
  cd backend
```
- Install all the requirments
```bash
  pip install -r requirments.txt
```
- Run the server (default port: http://127.0.0.1:8000)
```bash
  uvicorn main:app
```
- Already hosted server could be found on 
```bash
  https://farmconnectback.onrender.com/docs
```
- When hosting on server, you can use the Dockerfile provided to containerize the program to avoid any dependency issues.

### Generating and Testing APK (frontend)
- Frontend is developed on Android studios
- Change the endpoint URL to your own backend URL.
- Use 10.0.2.2:8000 to access the localhost.
- Generate the .apk file from the Android Studios


## 🐄API Documentation
- The project provides API endpoints for the developers to implement them in their own projects, extensions or apps.
- API Documentation is simple and is available at http://127.0.0.1:8000/docs
- ![Alt text](image-4.png)


## Team Members:

| S.No. | Name | Role | GitHub Username:octocat: |
| --------------- | --------------- | --------------- | --------------- |
| 1. | Ansh Anand | Backend Development| [@HonestFreak](https://www.github.com/HonestFreak)  |
| 2. | Thota Rajeev | Frontend Development | [@rajeev210403](https://github.com/rajeev210403) |
| 3. | Karthik Prasad S | Backend Development | [@karthikprasads](https://github.com/karthikprasads) |
| 4. | Nithin Chepuri | Frontend Development| [@NithinChepuri](https://github.com/NithinChepuri) |
| 5. | Sai Vignesh | Frontend Development | [@SaiVignesh-K](https://github.com/SaiVignesh-K)  |


## License

The Project is Opensource. Feel free to use or modify the code.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)




