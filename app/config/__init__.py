from .kafka_settings import kafka_settings, KafkaSettings
from .mongo_settings import mongo_settings, MongoSettings
from .redis_settings import redis_settings, RedisSettings
from .twitch_settings import twitch_settings, TwitchSettings


class Settings:
    def __init__(self, mongo_settings: MongoSettings, kafka_settings: KafkaSettings, redis_settings: RedisSettings,
                 twitch_settings: TwitchSettings, fastapi_settings: FastAPISettings):
        self.mongo_settings = mongo_settings
        self.kafka_settings = kafka_settings
        self.redis_settings = redis_settings
        self.twitch_settings = twitch_settings
        self.fastapi_settings = fastapi_settings


settings = Settings(mongo_settings, kafka_settings, redis_settings, twitch_settings)
