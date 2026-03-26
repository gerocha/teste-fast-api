from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

from stock.repository.item import get_items
from stock.schemas.item import ItemSchema


class GetItemsUseCase:
    session: Annotated[Session, Depends] | None = None

    def __init__(self, session: Annotated[Session, Depends]) -> None:
        self.session = session

    def execute(self):
        if not self.session:
            raise Exception('missing session')
        objects = get_items(session=self.session)

        return [ItemSchema(
            name=i[1],
            description=i[2],
            price=i[3],
            quantity=i[4]
            ) for i in objects]
