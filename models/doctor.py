from sqlalchemy import Column, String, Integer, ForeignKey, VARCHAR
from datetime import datetime
from sqlalchemy.orm import relationship
from .base import Base


class Doctor(Base):
     # Tablename
    __tablename__ = "doctors"

    # Table structure
    id = Column(Integer(), primary_key= True)
    name  = Column(VARCHAR(), nullable=False)
    specialization  = Column(String(), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    date = Column(Integer())


    def __init__(self,name,specialization ,date=None):
        self.name = name
        self.specialization  = specialization 
        self.date = date if date is not None else datetime.now().year
    pass          