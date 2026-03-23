from sqlalchemy import Numeric, Table, Column, Integer, String
from stock.infra.db import metadata

item_table = Table(
        "item",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
        Column("price", Numeric(precision=10, scale=2)),
        Column("quantity_in_stock", Integer),
        )
