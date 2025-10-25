from fastapi import FastAPI
from .routes import index_router


app = FastAPI(
    title="home"
)

app.include_router(index_router)