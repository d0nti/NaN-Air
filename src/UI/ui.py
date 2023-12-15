from UI.voyages import Voyages
from UI.employees import Employees
from UI.destinations import Destinations
from UI.airplanes import Airplanes
from UI.Utils.Constants import UIConstants
from Logic.UILogicWrapper import UI_Logic_Wrapper
from UI.Utils.Constants import UIConstants


class MainMenu:
    def __init__(self):
        self.logic_wrapper = UI_Logic_Wrapper()
        self.voyages = Voyages(self.logic_wrapper)
        self.employees = Employees(self.logic_wrapper)
        self.destinations = Destinations(self.logic_wrapper)
        self.airplanes = Airplanes(self.logic_wrapper)

    def main_menu_output(self):
        print(UIConstants.HEADER.format(UIConstants.BOOKING_SYSTEM))
        print(
                UIConstants.MAIN_MENU_OPTION.format(
                UIConstants.MANAGE_VOYAGES,
                UIConstants.MANAGE_EMPLOYEES,
                UIConstants.MANAGE_DESTINATIONS,
                UIConstants.MANAGE_AIRPLANES,
                UIConstants.QUIT,
            )
        )

    def show_main_menu(self):
        self.main_menu_output()
        return input("User Input: ").lower()

    def control_main_menu(self):
        while (command := self.show_main_menu()) not in ("q", "q."):
            if command == "1" or command == "1.":
                self.voyages.input_prompt_voyages()
            elif command == "2" or command == "2.":
                self.employees.control_employee_menu() 
            elif command == "3" or command == "3.":
                self.destinations.control_destination_menu()
            elif command == "4" or command == "4.":
                self.airplanes.control_airplane_menu()
            else:
                print(UIConstants.INVALID_INPUT)
        print(UIConstants.QUIT_MESSAGE)
        # end while command
