from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL 
from sqlalchemy.orm import sessionmaker

#https://fastapi.tiangolo.com/tutorial/sql-databases/

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:@localhost:5432/ovaldb"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()