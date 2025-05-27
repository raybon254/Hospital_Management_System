from sqlalchemy import Column, String, Integer, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Department(Base):
    # Tablename
    __tablename__ = "departments"

    # Table structure
    id = Column(Integer(), primary_key= True)
    name  = Column(VARCHAR(), nullable=False)
    date = Column(Integer())


    def __init__(self,name,date=None):
        self.name = name
        self.date = date if date is not None else datetime.now().year
    pass