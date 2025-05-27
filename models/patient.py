from sqlalchemy import Column, String, Integer, VARCHAR
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Patient(Base):
    # Tablename
    __tablename__ = "patients"

    # Table structure
    id = Column(Integer(), primary_key= True)
    name  = Column(VARCHAR(), nullable=False)
    age = Column(Integer(), nullable=False)
    date = Column(Integer())

    # Relationships
    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete-orphan")


    def __init__(self,name,age,date=None):
        self.name = name
        self.age = age
        self.date = date if date is not None else datetime.now().year
    pass