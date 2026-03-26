from fastapi import APIRouter

from stock.dependencies import SessionDep
from stock.repository.item import insert_item_from_schema
from stock.schemas.item import ItemSchema
from stock.services.logger import logger
from stock.use_cases.get_items import GetItemsUseCase


router = APIRouter(prefix="/items")


@router.post("/", status_code=201)
async def insert_item(item: ItemSchema, session: SessionDep):
    logger.info("Inserting new item")
    insert_item_from_schema(session, item)

@router.get('/')
async def get_items(session: SessionDep):
    use_case = GetItemsUseCase(session)
    return use_case.execute()
