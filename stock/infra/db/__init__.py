from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

connect_args = {"check_same_thread": False}
engine = create_engine(
    "sqlite+pysqlite:///:memory:", echo=True, connect_args=connect_args
)

metadata = MetaData()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
