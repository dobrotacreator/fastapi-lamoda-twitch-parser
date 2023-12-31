import logging

from fastapi import APIRouter, HTTPException

from core.mongo import MongoDBService
from models.lamoda import Product, Task
from services.kafka import KafkaService

router = APIRouter(prefix="/lamoda")
mongo_service = MongoDBService()
logging.basicConfig(level=logging.INFO)


@router.post("/parsing_task")
async def create_parsing_task(task: Task):
    kafka = KafkaService()
    await kafka.send_message("parse", "core.lamoda_parser@parse_lamoda@" + task.category_url)
    return {"message": "Parsing task created successfully"}


@router.post("/products")
async def create_product(product: Product):
    mongo_service.insert_document("lamoda_products", product.dict())
    return {"message": "Product created successfully"}


@router.get("/products", response_model=dict[str, list[Product]])
async def get_products():
    cursor = mongo_service.find_documents("lamoda_products", {})
    products = []
    for product in cursor:
        product['_id'] = str(product['_id'])
        products.append(product)
    return {"products": products}


@router.get("/products/{product_id}", response_model=dict[str, Product])
async def get_product(product_id: str):
    query = {"_id": product_id}
    product = mongo_service.find_documents("lamoda_products", query)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": product}


@router.put("/products/{product_id}")
async def update_product(product_id: str, product: Product):
    query = {"_id": product_id}
    update = {"$set": product.dict()}
    mongo_service.update_document("lamoda_products", query, update)
    return {"message": "Product updated successfully"}


@router.delete("/products/{product_id}")
async def delete_product(product_id: str):
    query = {"_id": product_id}
    mongo_service.delete_document("lamoda_products", query)
    return {"message": "Product deleted successfully"}
