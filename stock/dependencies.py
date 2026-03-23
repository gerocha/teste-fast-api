from typing import Annotated

from fastapi import Depends
from sqlalchemy import Connection
from stock.infra.db import engine


def get_connection():
    with engine.connect() as conn:
        yield conn


SessionDep = Annotated[Connection, Depends(get_connection)]
