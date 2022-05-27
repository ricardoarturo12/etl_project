from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from dotenv import dotenv_values


config = dotenv_values(".env")
DATABASE = config["DATABASE_URL"]

# crear database consolidado

SQLALCHEMY_DATABASE_URL = f'{DATABASE}?sslmode=prefer'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


