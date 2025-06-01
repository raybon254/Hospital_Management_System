Hospital Management System

A command-line based hospital management system built with Python 3, SQLAlchemy ORM, and SQLite, designed to manage the core operations of a hospital: tracking departments, doctors, patients, and appointments.
Demo

Watch a full walkthrough of the system here:

    🎥 Loom Video Walkthrough :
    
            https://www.loom.com/share/65ba7c94fc674c049c5e0c6d0a77aa36?sid=f36396a3-1da0-4f3d-bfd7-bf9c94ea1723
    
    🗃️ Database Schema: 
            
            https://dbdiagram.io/d/Hospital-DB-relationship-schema-6834a1d56980ade2eb782076

View the full database relationship schema on dbdiagram.io:
Hospital DB Relationship Schema
Table of Contents

    Features
    Tech Stack
    Setup Instructions
    Usage
    Database Models
    Example Commands
    Future Improvements

Features

    Add, view, update, and delete:

        🏥 Departments
        👨‍⚕️ Doctors
        🧑‍🦰 Patients
        📅 Appointments

    Automatically:

        Link doctors to departments
        Link appointments to both patients and doctors
    Displays readable information (e.g., names instead of foreign key IDs)

    Prevents double-booking of appointments (optional logic)
    CLI-based interface for smooth user interaction
    Persistent data storage using SQLite

Tech Stack

    Python 3.x
    SQLAlchemy (ORM for database interaction)
    SQLite (lightweight local database)
    Optional: tabulate for better CLI table display

Setup Instructions

    Clone the repo
        git clone https://github.com/raybon254/Hospital_Management_System.git
        cd HOSPITAL_MANAGEMENT-SYSTEM

Create a virtual environment (optional but recommended)
    python3 -m venv venv
    source venv/bin/activate 
    # On Windows: venv\Scripts\activate

Run the main application

    python main.py

Usage

    Use the menu-driven CLI to:

        Manage departments
        Assign doctors
        Register patients
        Schedule and manage appointments
    Navigate using numbered options

Database Models

    Department
        id, name

    Doctor
        id, name, specialty, department_id

    Patient
        id, name, age, gender

    Appointment
        id, patient_id, doctor_id, date, time

Refer to the Hospital DB Relationship Schema for a visual model.

    https://dbdiagram.io/d/Hospital-DB-relationship-schema-6834a1d56980ade2eb782076
    
💻 Example Commands

# Add a department
Enter department name: Cardiology

# Register a new doctor
Enter doctor name: Dr. Smith  
Enter specialty: Cardiology  
Select department: Cardiology

# Register a patient
Enter patient name: Alice Johnson  
Enter age: 32  
Enter gender: Female

# Schedule an appointment
Enter appoinment name: Surgery 
Enter date (YYYY-MM-DD HH:MM): 2025-06-01  10:30
Enter doctor: Dr.Smith
Enter patient: Alice Johnson


