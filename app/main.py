from fastapi import FastAPI

from routers import lamoda
from utils import exeption_handler

app = FastAPI()

app.add_exception_handler(Exception, exeption_handler.exception_handler)
app.include_router(lamoda.router)
