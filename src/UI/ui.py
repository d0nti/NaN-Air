from UI.voyages import Voyages
from UI.employees import Employees
from UI.destinations import Destinations
from UI.airplanes import Airplanes
from Logic.UILogicWrapper import UI_Logic_Wrapper
import sys


DASH_SYMBOL = "-"
LENGTH_SYMBOL = 30 
INVALID_INPUT = "Invalid input! Please try again."
QUIT_MESSAGE = "Bye Bye!"


HEADER = (
    f"{DASH_SYMBOL * LENGTH_SYMBOL}"
    + "\n"
    + "  NaN Air - {}"
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

class MainMenu:
    def __init__(self):
        self.logic_wrapper = UI_Logic_Wrapper()
        self.voyages = Voyages(self.logic_wrapper)
        self.employees = Employees(self.logic_wrapper)
        self.destinations = Destinations(self.logic_wrapper)
        self.airplanes = Airplanes(self.logic_wrapper)

    def menu_output(self):
        print(HEADER.format("Booking System"))
        print(MAIN_MENU)


    def input_prompt_mainmenu(self):
            
        while True:
            
            self.menu_output()
            while True:
                command = input("User Input: ").lower()

                if command == "1" or command == "1.":
                    
                    self.voyages.input_prompt_voyages()
                    back = self.voyages.input_prompt_voyages()
                    if back == "b" or back =="b.":
                        break

                elif command == "2" or command == "2.":
                    # self.employees.input_prompt_employees() # LES INPUT
                    
                    self.employees.employees_menu_output() # PRENTAR MENU
                    back = self.employees.input_prompt_employees() # LES INPUT. SETT Í BREYTU TIL ÞESS AÐ GETA KALLAÐ Á HANA RÉTT TIL AÐ FARA TILBAKA 
                    if back == "b":
                        break
                
                elif command == "3" or command == "3.":
                    
                    back = self.destinations.input_prompt_destinations() # LES INPUT
                    if back == "b":
                        break

                elif command == "4" or command == "4.":
                    
                    self.airplanes.airplanes_menu_output()
                    back = self.airplanes.input_prompt_airplanes()
                    if back == "b":
                        break
                    
                elif command == "q" or command == "q.":
                    
                    print(QUIT_MESSAGE)
                    sys.exit()

                else:
                    
                    print("Invalid input! Please try again")
                    self.menu_output()  
