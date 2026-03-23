from typing import Annotated
from fastapi import Depends
from sqlalchemy import insert
from sqlalchemy.orm import Session
from stock.schemas.item import ItemSchema
from stock.infra.db.mysql.models.item import item_table


def insert_item_from_schema(connection: Annotated[Session, Depends], item: ItemSchema):
    stmt = insert(item_table).values(
        name=item.name,
        description=item.description,
        price=item.price,
        quantity_in_stock=item.quantity,
    )

    connection.execute(stmt)
    connection.commit()
