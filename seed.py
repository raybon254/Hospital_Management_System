#seed Hospitals.DB
from models.base import session,create_table,drop_table
from models import Appointment,Department,Patient,Doctor
from datetime import datetime

# Clear and recreate all tables (optional)
drop_table()
create_table()

# Departments
cardiology = Department(name='Cardiology')
neurology = Department(name='Neurology')
session.add_all([cardiology, neurology])
session.commit()

# Doctors
dr_smith = Doctor(name='John Smith', specialization='Cardiologist', department=cardiology)
dr_lee = Doctor(name='Susan Lee', specialization='Neurologist', department=neurology)
session.add_all([dr_smith, dr_lee])
session.commit()

#Patients
alice = Patient(name='Alice Johnson', age=30, gender='Female')
bob = Patient(name='Bob Miller', age=45, gender='Male')
session.add_all([alice, bob])
session.commit()

#Appointments
appt1 = Appointment(appointment_name="Therapy", appointment_date=datetime(2025, 6, 5, 14, 30), doctor=dr_smith, patient=alice)
appt2 = Appointment(appointment_name="Surgery", appointment_date=datetime(2025, 6, 6, 10, 00), doctor=dr_lee, patient=bob)
session.add_all([appt1, appt2])
session.commit()

print("✅ Seed data inserted successfully.")
