from Logic.logic import EmployeeLogic
from Model.employee import Employee

class MainMenu:
    def __init__(self):
        self.employee_logic = EmployeeLogic(Employee)

    def menu_output(self):
        print("------------------------------")
        print("NaN Air - Booking System")
        print("------------------------------")
        print("1. Manage Voyages")
        print("2. Manage Employees")
        print("3. Manage Destinations")
        print("4. Manage Aircrafts")

    def input_prompt(self):
        while True:  #BREYTA?
            self.menu_output()
            command = input("User Input: ")
            command = command.lower()
            if command == "q":
                print("Bye Bye!")
                break
            elif command == "1" or "1.":
                pass
            
            elif command == "2" or "2.":
                pass
            
            elif command == "3" or "3.":
                pass

            elif command == "4" or "4.":
                pass