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

    department = relationship("Department", back_populates="doctors")
    
    # Relationships
    appointments = relationship("Appointment", back_populates="doctor", cascade="all, delete-orphan")


    def __init__(self,name,specialization,department,date=None):
        self.name = name
        self.specialization  = specialization
        self.department  = department
        self.date = date if date is not None else datetime.now()
    pass          