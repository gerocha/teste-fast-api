from fastapi import FastAPI
from stock.routers import item

app = FastAPI()

app.include_router(item.router)
