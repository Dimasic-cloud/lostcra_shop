from fastapi import FastAPI
from .routes import index_router
from .models import *


app = FastAPI()

app.include_router(index_router)