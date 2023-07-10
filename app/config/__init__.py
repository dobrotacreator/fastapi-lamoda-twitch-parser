from pydantic_settings import BaseSettings

from .fastapi_settings import fastapi_settings, FastAPISettings
from .kafka_settings import kafka_settings, KafkaSettings
from .mongo_settings import mongo_settings, MongoSettings
from .redis_settings import redis_settings, RedisSettings
from .twitch_settings import twitch_settings, TwitchSettings


class Settings(BaseSettings):
    mongo_settings: MongoSettings = mongo_settings
    kafka_settings: KafkaSettings = kafka_settings
    redis_settings: RedisSettings = redis_settings
    twitch_settings: TwitchSettings = twitch_settings
    fastapi_settings: FastAPISettings = fastapi_settings


settings = Settings()
