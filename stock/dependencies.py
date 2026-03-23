from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from stock.infra.db import SessionLocal


def get_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionDep = Annotated[Session, Depends(get_connection)]
