from fastapi import APIRouter, HTTPException

from core.mongo import MongoDBService
from models.lamoda_models import Product

router = APIRouter(prefix="/lamoda")
mongo_service = MongoDBService()


@router.post("/products")
def create_product(product: Product):
    mongo_service.insert_document("lamoda_products", product.dict())
    return {"message": "Product created successfully"}


@router.get("/products")
def get_products():
    products = list(mongo_service.find_documents("lamoda_products", {}))
    return {"products": products}


@router.get("/products/{product_id}")
def get_product(product_id: str):
    query = {"_id": product_id}
    product = mongo_service.find_documents("lamoda_products", query)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": product}


@router.put("/products/{product_id}")
def update_product(product_id: str, product: Product):
    query = {"_id": product_id}
    update = {"$set": product.dict()}
    mongo_service.update_document("lamoda_products", query, update)
    return {"message": "Product updated successfully"}


@router.delete("/products/{product_id}")
def delete_product(product_id: str):
    query = {"_id": product_id}
    mongo_service.delete_document("lamoda_products", query)
    return {"message": "Product deleted successfully"}
