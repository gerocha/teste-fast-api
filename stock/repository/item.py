from typing import Annotated
from sqlalchemy import insert
from stock.schemas.item import ItemSchema
from stock.infra.db.mysql.models.item import item_table


def insert_item_from_schema(connection: Annotated, item: ItemSchema):
    stmt = insert(item_table).values(
            name=item.name,
            description=item.description,
            price=item.price,
            quantity_in_stock=item.quantity
            )

    connection.execute(stmt)
    connection.commit()
