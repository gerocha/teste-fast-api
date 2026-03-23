from sqlalchemy import MetaData, create_engine

engine = create_engine("sqlite+pysqlite:///:memory:",
                       echo=True)

metadata = MetaData()
