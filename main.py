from models.base import session,create_table
from models import *
from helper import (
    add_dep, all_dep, update_dep, del_dep,
    add_doc, all_doc, update_doc, del_doc,
    add_app, all_app, update_app, del_app,
    add_pat, all_pat, update_pat, del_pat,
)




# CLI Routing
def hospital_ops():
    tables = {
        '1': ("Departments", {
            '1': add_dep,
            '2': all_dep,
            '3': update_dep,
            '4': del_dep,
        }),
        '2': ("Doctors", {
            '1': add_doc,
            '2': all_doc,
            '3': update_doc,
            '4': del_doc,
        }),
        '3': ("Appointments", {
            '1': add_app,
            '2': all_app,
            '3': update_app,
            '4': del_app,
        }),
        '4': ("Patients", {
            '1': add_pat,
            '2': all_pat,
            '3': update_pat,
            '4': del_pat,
        }),
    }

    while True:
        print("\nChoose table to work on:")
        for key, (label, _) in tables.items():
            print(f"{key}: {label}")
        choice = input("Enter an option (or 'q' to quit): ")

        if choice == 'q':
            break
        if choice in tables:
            _, actions = tables[choice]
            print("\nChoose action:")
            print("1: Add\n2: View All\n3: Update\n4: Delete")
            action_choice = input("Enter action: ")
            if action_choice in actions:
                actions[action_choice]()
            else:
                print("Invalid action.")
        else:
            print("Invalid table selection.")

if __name__ == "__main__":
    hospital_ops()