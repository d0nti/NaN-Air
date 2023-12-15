from UI.voyages import Voyages
from UI.employees import Employees
from UI.destinations import Destinations
from UI.airplanes import Airplanes
from UI.Utils.Constants import UIConstants
from Logic.LogicWrapper import UI_Logic_Wrapper
from UI.Utils.Constants import UIConstants


class MainMenu:
    def __init__(self):
        """ We establish a link from the main ui file (this file)
            to the logic wrapper class to be able to call functions
            from other layers through that class.
            We then ensure that all other classes that we will need
            to call are also initialized by calling them with the
            instance of the logic wrapper class we initialized
        """
        self.logic_wrapper = UI_Logic_Wrapper()
        self.voyages = Voyages(self.logic_wrapper)
        self.employees = Employees(self.logic_wrapper)
        self.destinations = Destinations(self.logic_wrapper)
        self.airplanes = Airplanes(self.logic_wrapper)

    def main_menu_output(self):
        """ Prints the main menu of the program, showing that the user 
            can interface with Voyages, Employees, Destinations, and 
            Airplanes from this point in the software
        """
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
        """ This function calls the function above whilst
            also taking in where the user wants to manoeuvre
        """
        self.main_menu_output()
        return input("User Input: ").lower()

    def control_main_menu(self):
        """ Reads the input taken from the show_main_menu
            function and calls the appropriate function
            through the established connection in the 
            __init__
        """
        while (command := self.show_main_menu()) not in ("q", "q."):
            if command == "1" or command == "1.":
                self.voyages.control_voyage_menu()
            elif command == "2" or command == "2.":
                self.employees.control_employee_menu() 
            elif command == "3" or command == "3.":
                self.destinations.control_destination_menu()
            elif command == "4" or command == "4.":
                self.airplanes.control_airplane_menu()
            else:
                print(UIConstants.INVALID_INPUT)
        print(UIConstants.QUIT_MESSAGE)
