from models.base import session,create_table,drop_table
from models import Appointment,Department,Patient,Doctor


# CRUD operations for all classes
# Utility functions
# Dep
def get_department(dep_name):
    return session.query(Department).filter_by(name=dep_name).first()
# Doc
def get_doctor(doc_name):
    return session.query(Doctor).filter_by(name=doc_name).first()

# Pat
def get_patient(pat_name):
    return session.query(Patient).filter_by(name=pat_name).first()

# App
def get_appointment(app_name):
    return session.query(Appointment).filter_by(appointment_name=app_name).first()


def get_date_validation(app_date):
     from datetime import datetime

     try:
        date_obj = datetime.strptime(app_date, "%Y-%m-%d %H:%M")
        return date_obj
     except ValueError:
          return None


def delete_action(prompt: str) ->bool:
    return input(f"{prompt} (Yes/No):").strip().lower() == 'yes'


# CRUD operations
# Department
# Add
def add_dep():
    dep_name = input("Enter department name:")

    if get_department(dep_name):
        print(f"Department already exists.")
        return
    try:
        session.add(Department(name=dep_name))
        session.commit()
        print(f"Department added successfully")

    except Exception as e:
        print(f"Error adding Department: {e}")

# Read(list all departments)
def all_dep():
    deps = session.query(Department).all()
    for d in deps:
        print(d.name)


# Update
def update_dep():
    department = input("Enter department:")

    department = get_department(department)
    if department:
        new_department = input("Enter updated_department:")
        department.name = new_department
        session.commit()
        print("Department updated successfully.")
    else:
        print("Department not found.")


# Delete
def del_dep():
    department_name = input("Enter department:")
    department = get_department(department_name)

    if department:
        if delete_action("Confirm you want to delete department:"):
            session.delete(department)
            session.commit()
            print(f"Deleted successfully.")
        else:
            print(f"Deletion cancelled!")
    else:
        print(f"Department not found")

# Doctor
    # Add
def add_doc():
        doc_name = input("Enter doctor name: ")
        doc_specs = input("Enter Doctor's specialization : ")

        # Get department
        dep_name = input("Enter department for doctor: ")
        department = get_department(dep_name)
        if not department:
            print("Department not found.")
            return

        # Check if doctor already exists
        existing_doctor = get_doctor(doc_name)
        if existing_doctor:
            print("Doctor already exists.")
            return

        # Create and add doctor with department
        doctor = Doctor(name=doc_name, specialization=doc_specs  ,department=department)

        try:
            session.add(doctor)
            session.commit()
            print("Doctor added successfully!")
        except Exception as e:
            print(f"Error adding Doctor: {e}")
    # Read
def all_doc():
        docs = session.query(Doctor).all()
        for d in docs:
            print(d.name)


    # Update
def update_doc():
        doctor_name = input("Enter doctor:")

        doctor = get_doctor(doctor_name)
        if doctor:
            new_doctor = input("Enter updated_doctor:")
            doctor.name = new_doctor
            session.commit()
            print("Doctor updated successfully.")
        else:
            print("Doctor not found.")


    # Delete
def del_doc():
        doctor_name = input("Enter doctor:")
        doctor = get_doctor(doctor_name)
        if doctor:
            if delete_action("Confirm you want to delete doctor:"):
                session.delete(doctor)
                session.commit()
                print(f"Deleted successfully.")
            else:
                print(f"Deletion cancelled!")
        else:
            print(f"Doctor not found")

# Appointment
    # Add
def add_app():
            from datetime import datetime
            app_name = input("Enter appointment name: ")

            # validate date
            app_date = input("Enter appointment date and time(YYYY-MM-DD HH:MM): ")
            date = get_date_validation(app_date)
            if not date:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
            elif date < datetime.now():
                 print("Date and time can't be in the past!")
            else:
                print("Date accepted:", date)

        # Fetch Doctor
            doc_name = input("Enter doctor name for appointment: ")
            doctor = get_doctor(doc_name)
            if not doctor:
                print("Doctor not found.")
                return

            # Fetch Patient
            pat_name = input("Enter patient name for appointment: ")
            patient = get_patient(pat_name)
            if not patient:
                print("Patient not found.")
                return

            # Create Appointment with relationships
            appointment = Appointment(appointment_name= app_name, appointment_date=date, doctor=doctor, patient=patient)

            try:
                session.add(appointment)
                session.commit()
                print("Appointment added successfully!")
            except Exception as e:
                print(f"Error: {e}")

    # Read
def all_app():
        apps = session.query(Appointment).all()
        for a in apps:
            print(f"{a.patient.name} has an appointment with {a.doctor.name} on {a.appointment_date}")

    # Update
def update_app():
        appoinment_name = input("Enter Appointment name:")

        appointment = get_appointment(appoinment_name)
        if appointment:
            new_appointment = input("Enter updated_appointment:")
            new_appointment_date = input("Enter updated_date:")
            appointment.appointment_name = new_appointment
            appointment.appointment_date = new_appointment_date
            session.commit()
            print("Appointment updated successfully.")
        else:
            print("Appointment not found.")


    # Delete
def del_app():
        appointment_name = input("Enter appointment:")
        appointment = get_appointment(appointment_name)

        if appointment:
            if delete_action("Confirm you want to delete appointment:"):
                session.delete(appointment)
                session.commit()
                print(f"Deleted successfully.")
            else:
                print(f"Deletion cancelled!")
        else:
            print(f"Appointment not found")

# Patient
    #Add
def add_pat():
        pat_name = input("Enter patient's name:")
        pat_age = input("Enter patient's age:")
        pat_gender = input("Enter patient's gender:")
        
        if get_patient(pat_name):
            print(f"Patient already exists.")
            return
        try:
            session.add(Patient(name = pat_name, age=pat_age,gender=pat_gender))
            session.commit()
            print(f"Patient added successfully")

        except Exception as e:
            print(f"Error adding Patient: {e}")

    # Read
def all_pat():
        pats = session.query(Patient).all()
        for p in pats:
            print(p.name)

    # Update
def update_pat():
        patient = input("Enter patient:")

        patient = get_patient(patient)
        if patient:
            new_patient = input("Enter updated_patient:")
            patient.name = new_patient
            session.commit()
            print("Patient updated successfully.")
        else:
            print("Patient not found.")


    # Delete
def del_pat():
        patient_name = input("Enter patient:")        
        patient = get_patient(patient_name  )      

        if patient:
            if delete_action("Confirm you want to delete patient:"):
                session.delete(patient)
                session.commit()
                print(f"Deleted successfully.")
            else:
                print(f"Deletion cancelled!")
        else:
            print(f"patient not found")
