from datetime import datetime

from pymongo import MongoClient

from config.mongo_settings import mongo_settings


class MongoDBService:
    def __init__(self):
        self.client = MongoClient(
            host=mongo_settings.host,
            port=mongo_settings.port,
        )
        self.db = self.client[mongo_settings.database]

    def insert_document(self, collection_name, document):
        collection = self.db[collection_name]
        document["created_at"] = datetime.now().time()
        collection.insert_one(document)

    def find_documents(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find(query)

    def update_document(self, collection_name, query, update):
        collection = self.db[collection_name]
        collection.update_one(query, update)

    def delete_document(self, collection_name, query):
        collection = self.db[collection_name]
        collection.delete_one(query)
