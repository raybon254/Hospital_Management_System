from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Appointment(Base):
    # Tablename
    __tablename__ = "appointments"

    # Table structure
    id = Column(Integer(), primary_key= True)
    appointment_date = Column(Integer(), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    date = Column(Integer())

    # Relationships
    doctor = relationship("Doctor" ,back_populates="appointments")
    patient = relationship("Patient" ,back_populates="appointments")

    def __init__(self,appointment_date,date=None):
        self.appointment_date = appointment_date
        self.date = date if date is not None else datetime.now()
    pass