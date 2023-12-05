from Logic.logic import EmployeeLogic
from Model.employee import Employee
from UI.voyages import Voyages
<<<<<<< Updated upstream
=======
from UI.employees import Employees
>>>>>>> Stashed changes


BOOKING_SYSTEM = "Booking System"
MANAGE_EMPLOYEES = "Manage Employees"
MANAGE_AIRPLANES = "Manage Airplanes"
MANAGE_DESTINATIONS = "Manage Destinations"
MANAGE_VOYAGES = "Manage Voyages"
DASH_SYMBOL = "-"
LENGTH_SYMBOL = 30


HEADER = (
    f"{DASH_SYMBOL * LENGTH_SYMBOL}"
    + "\n"
    + "  NaN Air - {location}"
    + "\n"
    + f"{DASH_SYMBOL * LENGTH_SYMBOL}"
)

# HEADER_MAIN_MENU = (
#     "------------------------------"
#     + "\n"
#     + "  NaN Air - Booking System"
#     + "\n"
#     + "------------------------------
# )

MAIN_MENU = (

    "1. Manage Voyages"
    + "\n"
    + "2. Manage Employees"
    + "\n"
    + "3. Manage Destinations"
    + "\n"
    + "4. Manage Aircrafts"
    + "\n"
    + "q. Quit"
)


AIRPLANE_MENU = (
    "1. Register Aircraft"
    + "\n"
    + "2. M"
    + "\n"
    + "3. Manage Destinations"
    + "\n"
    + "4. Manage Aircrafts"
    + "\n"
    + "q. Quit"
)


class MainMenu:
    def __init__(self):
        self.employee_logic = EmployeeLogic(Employee)
        self.voyages = Voyages()
<<<<<<< Updated upstream
=======
        self.employees = Employees()
>>>>>>> Stashed changes

    def menu_output(self):
        print(HEADER)
        print(MAIN_MENU)

    def input_prompt_mainmenu(self):
        self.menu_output()
        while True:
            command = input("User Input: ").lower()
            if command == "1" or command == "1.":
<<<<<<< Updated upstream
                self.voyages.voyages_menu_output() # PRENTAR MENU
                self.voyages.input_prompt_voyages() # LES INPUT
=======
                self.voyages.voyages_menu_output()
                self.voyages.input_prompt_voyages()
>>>>>>> Stashed changes
            elif command == "2" or command == "2.":
                self.employees.employees_menu_output()
                self.employees.input_prompt_employees()
            elif command == "3" or command == "3.":
                pass
            elif command == "4" or command == "4.":
                pass
            elif command == "q":
                print("Bye Bye!")
                break
            else:
                print("Invalid input! Please try again")
                self.menu_output()  
