from typing import Annotated, Any, Sequence
from fastapi import Depends
from sqlalchemy import insert, select
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


def get_items(session: Annotated[Session, Depends]) -> Sequence[Any]:
    stmt = select(item_table)

    objects = session.execute(stmt).all()
    return objects
