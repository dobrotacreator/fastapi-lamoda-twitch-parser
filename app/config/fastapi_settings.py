from pydantic import BaseSettings


class FastAPISettings(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = 'FASTAPI_'
        env_file = ".env"


fastapi_settings = FastAPISettings()
