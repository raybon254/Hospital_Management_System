from models.base import Base,session,engine
from models import Appointment,Department,Patient,Doctor

def hospital():
    Base.metadata.create_all(engine)
    print("Creating db")

    # patients obj
    mercy = Patient(name="Mercy",age=24)
    ray = Patient(name="Ray",age=27)

    session.add_all([mercy,ray])

    # departments obj
    medical = Department(name="Medical")
    specialty = Department(name="Specialty")

    session.add_all([medical,specialty])

    # doctors obj
    john = Doctor(name="John",specialization="surgeon", department= medical)
    mary = Doctor(name="mary",specialization="dermatologist",department= specialty)
    joy = Doctor(name="Joy",specialization="dermatologist",department= specialty)

    session.add_all([john,mary,joy])

    # appointments obj
    date1 = Appointment(appointment_date='30,5,2025' , doctor=john, patient = mercy)

    session.add_all([date1])
    session.commit()
    print("Done creating db")

def cli_phase():
    # CRUD operations for all classes
    # Utility functions
    # Department
        # Add
        dep = input("Enter department name:")
        
        # Read
        # Update
        # Delete
    # Doctor
        # Add
        # Read
        # Update
        # Delete
    # Patient
        # Add
        # Read
        # Update
        # Delete
    # Appointment
        #Add
        # Read
        # Update
        # Delete
    pass 

if __name__ == "__main__":
    hospital()