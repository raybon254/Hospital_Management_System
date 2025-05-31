from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///hospital.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# table creation
def create_table():
    Base.metadata.create_all(engine)

#drop table
def drop_table():
    Base.metadata.drop_all(engine)