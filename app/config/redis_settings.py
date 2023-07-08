from pydantic import BaseSettings


class RedisSettings(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = 'REDIS_'
        env_file = ".env"


redis_settings = RedisSettings()
