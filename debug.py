from models import Department, Patient, Doctor, Appointment
from models.base import session

def print_all_departments():
    print("=== Departments ===")
    departments = session.query(Department).all()
    if not departments:
        print("No departments found.")
    for d in departments:
        print(f"ID: {d.id} | Name: {d.name} ")
    print()

def print_all_patients():
    print("=== Patients ===")
    patients = session.query(Patient).all()
    if not patients:
        print("No patients found.")
    for p in patients:
        print(f"ID: {p.id} | Name: {p.name} | Age: {p.age} | Gender: {p.gender}")
    print()

def print_all_doctors():
    print("=== Doctors ===")
    doctors = session.query(Doctor).all()
    if not doctors:
        print("No doctors found.")
    for d in doctors:
        print(f"ID: {d.id} | Name: Dr. {d.name} | Department: {d.department.name if d.department else 'None'}")
    print()

def print_all_appointments():
    print("=== Appointments ===")
    appointments = session.query(Appointment).all()
    if not appointments:
        print("No appointments found.")
    for a in appointments:
        patient_name = a.patient.name if a.patient else "Unknown Patient"
        doctor_name = a.doctor.name if a.doctor else "Unknown Doctor"
        appt_time = a.appointment_date if a.appointment_date else "No Date"
        print(f"Appointment ID: {a.id} | Patient: {patient_name} | Doctor: Dr. {doctor_name} | Date & Time: {appt_time}")
    print()

if __name__ == "__main__":
    print_all_departments()
    print_all_patients()
    print_all_doctors()
    print_all_appointments()
