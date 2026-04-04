from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

from stock.settings import DB_URL

connect_args = {}

if 'sqlite' in DB_URL:
    connect_args = {"check_same_thread": False}

engine = create_engine(
    DB_URL, connect_args=connect_args
)

metadata = MetaData()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
