import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_NAME = os.getenv('DB_NAME')

DB_HOST = 'localhost'
DB_PORT = '5432'

DATABASE_URL = \
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def create_tables():
    # Initialize tables in db

    try:
        Base.metadata.create_all(engine)
        print("Tables successfully created.")
    except Exception as e:
        print(f"error 3 -> {e}")


class Job(Base):

    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    description = Column(String)


class Cv(Base):

    __tablename__ = 'cvs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    brute_text = Column(String)
    key_words = Column(String)
