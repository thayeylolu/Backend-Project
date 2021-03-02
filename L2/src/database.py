from sqlalchemy import create_engine # create the engine for connecting to the database
from sqlalchemy.ext.declarative import declarative_base #later imported into the models.py
from sqlalchemy.orm import sessionmaker #initialize a session in the databse

from decouple import config

SQLALCHEMY_DATABASE_URL = config("SQL_PATH")
engine = create_engine (SQLALCHEMY_DATABASE_URL, connect_args = {'check_same_thread':False})
SessionLocal = sessionmaker(autoflush = False, autocommit = False, bind = engine )
Base = declarative_base()

