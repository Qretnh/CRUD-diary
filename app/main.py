from db.connector import engine
from db.models.base import Base
from fastapi import FastAPI
from routers import notes


def create_app() -> FastAPI:
    app = FastAPI(title="Diary API")
    app.include_router(notes.router, prefix="/notes")
    return app


app = create_app()
