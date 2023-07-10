from fastapi import APIRouter, HTTPException

from core.mongo import MongoDBService
from models.twitch_models import Category, Channel

router = APIRouter(prefix="/twitch")
mongo_service = MongoDBService()


@router.post("/categories")
async def create_category(category: Category):
    mongo_service.insert_document("twitch_categories", category.dict())
    return {"message": "Category created successfully"}


@router.get("/categories")
async def get_categories():
    categories = list(mongo_service.find_documents("twitch_categories", {}))
    return {"categories": categories}


@router.get("/categories/{category_id}")
async def get_category(category_id: str):
    query = {"_id": category_id}
    category = mongo_service.find_documents("twitch_categories", query)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"category": category}


@router.put("/categories/{category_id}")
async def update_category(category_id: str, category: Category):
    query = {"_id": category_id}
    update = {"$set": category.dict()}
    mongo_service.update_document("twitch_categories", query, update)
    return {"message": "Category updated successfully"}


@router.delete("/categories/{category_id}")
async def delete_category(category_id: str):
    query = {"_id": category_id}
    mongo_service.delete_document("twitch_categories", query)
    return {"message": "Category deleted successfully"}


@router.post("/channels")
async def create_channel(channel: Channel):
    mongo_service.insert_document("twitch_channels", channel.dict())
    return {"message": "Channel created successfully"}


@router.get("/channels")
async def get_channels():
    channels = list(mongo_service.find_documents("twitch_channels", {}))
    return {"channels": channels}


@router.get("/channels/{channel_id}")
async def get_channel(channel_id: str):
    query = {"_id": channel_id}
    channel = mongo_service.find_documents("twitch_channels", query)
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    return {"channel": channel}


@router.put("/channels/{channel_id}")
async def update_channel(channel_id: str, channel: Channel):
    query = {"_id": channel_id}
    update = {"$set": channel.dict()}
    mongo_service.update_document("twitch_channels", query, update)
    return {"message": "Channel updated successfully"}


@router.delete("/channels/{channel_id}")
async def delete_channel(channel_id: str):
    query = {"_id": channel_id}
    mongo_service.delete_document("twitch_channels", query)
    return {"message": "Channel deleted successfully"}
