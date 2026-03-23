from fastapi import APIRouter

from stock.dependencies import SessionDep
from stock.repository.item import insert_item_from_schema
from stock.schemas.item import ItemSchema


router = APIRouter(
        prefix="/items"
        )


@router.post("/")
async def insert_item(item: ItemSchema, session=SessionDep):
    insert_item_from_schema(session, item)
