from fastapi import FastAPI
from stock.routers import item
from stock.infra.db import metadata, engine


def create_tables():
    metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()

app.include_router(item.router)
