import httpx

from config import settings
from models.twitch_models import Category, Channel
from core.mongo import MongoDBService


async def get_streams_by_filter(filter_type_with_query: str, limit=50):
    filter_type, query = filter_type_with_query.split('&')
    token_url = "https://id.twitch.tv/oauth2/token"
    token_params = {
        "client_id": settings.twitch_settings.client_id,
        "client_secret": settings.twitch_settings.client_secret,
        "grant_type": "client_credentials"
    }
    params = {
        "query": query,
        "first": limit
    }

    if filter_type == "categories":
        url = 'https://api.twitch.tv/helix/search/categories'
    elif filter_type == "channels":
        url = "https://api.twitch.tv/helix/search/channels"

    async with httpx.AsyncClient() as client:
        response_token = await client.post(token_url, data=token_params)
        data_token = response_token.json()
        headers = {
            "Client-ID": settings.twitch_settings.client_id,
            "Authorization": "Bearer " + data_token["access_token"]
        }
        response = await client.get(url, headers=headers, params=params)
        data = response.json()

    if response.status_code == 200:
        mongo_service = MongoDBService()
        if filter_type == "categories":
            categories = data["data"]
            for category in categories:
                category_id = category["id"]
                category_name = category["name"]
                twitch_category = Category(id=category_id, name=category_name)

                mongo_service.insert_document("twitch_categories", twitch_category.dict())
        else:
            channels = data["data"]
            for channel in channels:
                channel_name = channel["broadcaster_login"]
                game_name = channel["game_name"]
                twitch_channel = Channel(channel_name=channel_name, game_name=game_name)

                mongo_service.insert_document("twitch_channels", twitch_channel.dict())
    else:
        print(f"Error: {response.status_code} - {data['message']}")
