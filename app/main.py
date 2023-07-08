from fastapi import FastAPI
from services.mongo import MongoDBService

app = FastAPI()
mongo_service = MongoDBService()


@app.get("/")
async def root():
    mongo_service.insert_document("mycollection", {"name": "John Doe"})
    documents = mongo_service.find_documents("mycollection", {"name": "John Doe"})
    return {"documents": [doc for doc in documents]}
