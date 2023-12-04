from Logic.logic import EmployeeLogic
from Model.employee import Employee


class MainMenu:
    def __init__(self):
        self.employee_logic = EmployeeLogic(Employee)
        self.menu_options = {
            "1": self.manage_voyages,
            "1.": self.manage_voyages,
            "2": self.manage_employees,
            "2.": self.manage_employees,
            "3": self.manage_destinations,
            "3.": self.manage_destinations,
            "4": self.manage_aircrafts,
            "4.": self.manage_aircrafts,
            "q": self.quit_program,
        }

    def menu_output(self):
        print("------------------------------")
        print("  NaN Air - Booking System")
        print("------------------------------")
        print("1. Manage Voyages")
        print("2. Manage Employees")
        print("3. Manage Destinations")
        print("4. Manage Aircrafts")
        print("q. Quit")

    def input_prompt(self):
        while True:  # BREYTA?
            self.menu_output()
            command = input("User Input: ").lower()
            if command == "q":
                print("Bye Bye!")
                break
            elif command in self.menu_options:
                self.menu_options[command]()
            else:
                print("Invalid input! Please try again.")


    def voyages_menu_output(self):
        print("------------------------------")
        print("  NaN Air - Manage Voyages")
        print("------------------------------")
        print("1. Register Voyage")
        print("2. Edit Voyage")
        print("3. Populate Voyage")
        print("4. Display Voyages")
        print("5. Check Voyage Status")
        print("b. Back")
        print("q. Quit")

    def input_prompt(self):
        while True:
            self.voyages_menu_output()
            command = input("User Input: ")
            command = command.lower()
            if command == "q":
                print("Bye Bye!")
                break
            elif command == "b":
                break
            elif command == "1" or command == "1.":
                pass
            elif command == "2" or command == "2.":
                pass
            elif command == "3" or command == "3.":
                pass
            elif command == "4" or command == "4.":
                pass
            elif command == "5" or command == "5.":
                pass
            else:
                print("Invalid input! Please try again.")