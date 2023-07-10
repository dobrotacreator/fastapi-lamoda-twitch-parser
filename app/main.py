from fastapi import FastAPI

from routers import lamoda, twitch
from utils import exeption_handler
from config import settings

app = FastAPI()

app.add_exception_handler(Exception, exeption_handler.exception_handler)
app.include_router(lamoda.router)
app.include_router(twitch.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.fastapi_settings.host, port=settings.fastapi_settings.port)
