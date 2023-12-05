from UI.voyages import Voyages
from UI.employees import Employees
from UI.destinations import Destinations
from UI.airplanes import Airplanes
from Logic.UILogicWrapper import UI_Logic_Wrapper


BOOKING_SYSTEM = "Booking System"
MANAGE_EMPLOYEES = "Manage Employees"
MANAGE_AIRPLANES = "Manage Airplanes"
MANAGE_DESTINATIONS = "Manage Destinations"
MANAGE_VOYAGES = "Manage Voyages"
DASH_SYMBOL = "-"
LENGTH_SYMBOL = 30
QUIT = "quit"


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

    "1. {}"
    + "\n"
    + "2. {}"
    + "\n"
    + "3. {}"
    + "\n"
    + "4. {}"
    + "\n"
    + "q. {}"
)



"""MAIN_MENU = (

    "1. Manage Voyages"
    + "\n"
    + "2. Manage Employees"
    + "\n"
    + "3. Manage Destinations"
    + "\n"
    + "4. Manage Aircrafts"
    + "\n"
    + "q. Quit"
)"""


"""AIRPLANE_MENU = (
    "1. Register Aircraft"
    + "\n"
    + "2. "
    + "\n"
    + "3. Manage Destinations"
    + "\n"
    + "4. Manage Aircrafts"
    + "\n"
    + "q. Quit"
)"""


class MainMenu:
    def __init__(self):
        self.logic_wrapper = UI_Logic_Wrapper()
        self.voyages = Voyages(self.logic_wrapper)
        self.employees = Employees(self.logic_wrapper)
        self.destinations = Destinations(self.logic_wrapper)
        self.airplanes = Airplanes(self.logic_wrapper)

    def menu_output(self):
        print(HEADER.format(location = BOOKING_SYSTEM))
        print(MAIN_MENU)

    def input_prompt_mainmenu(self):
        self.menu_output()
        while True:
            command = input("User Input: ").lower()

            if command == "1" or command == "1.":
                self.voyages.voyages_menu_output() # PRENTAR MENU
                self.voyages.input_prompt_voyages() # LES INPUT

            elif command == "2" or command == "2.":
                self.employees.employees_menu_output() # PRENTAR MENU
                self.employees.input_prompt_employees() # LES INPUT

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
