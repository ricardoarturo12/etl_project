from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# crear database consolidado

SQLALCHEMY_DATABASE_URL = "postgresql://admin:12345@127.0.0.1:5455/consolidado?sslmode=prefer"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


