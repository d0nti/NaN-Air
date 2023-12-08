from Logic.UILogicWrapper import UI_Logic_Wrapper
from UI.Utils.Constants import UIConstants
from prettytable import PrettyTable
import sys


class Destinations:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper
        
        
    def destinations_menu_output(self):
        print(UIConstants.HEADER.format(UIConstants.MANAGE_DESTINATIONS))
        print(UIConstants.THREE_MENU_OPTION.format(UIConstants.DISPLAY_DESTINATIONS, UIConstants.REGISTER_NEW_DESTINATION, UIConstants.FIND_DESTINATION, UIConstants.BACK, UIConstants.QUIT))
        
        # print("1. Display Destinations")
        # print("2. Register Destination")
        # print("3. Find Destination")
        # print("b. Back")
        # print("q. Quit")

    def input_prompt_destinations(self):
        # self.destinations_menu_output()
        while True:
            command = input("User Input: ")
            command = command.lower()

            if command == "q" or command == "q.":
                print(UIConstants.QUIT_MESSAGE)
                sys.exit()

            elif command == "b" or command == "b.":
                return "b"

            elif command == "1" or command == "1.":
                self.list_destinations()

            elif command == "2" or command == "2.":
                self.register_destination()
                pass

            elif command == "3" or command == "3.":
                self.find_destination()
                pass

            else:
                print(UIConstants.INVALID_INPUT)


    def list_destinations(self):
        print(UIConstants.HEADER.format(UIConstants.DISPLAY_DESTINATIONS))

        destinations = self.logic_wrapper.get_all_destinations()
        
        
        if destinations:
            table = PrettyTable()
            table.field_names = ["Name", "Country", "Airport", "Flight Duration", "Distance from Iceland", "Contact Name", "Contact Phone Number"] 
            
            for destination in destinations:
                table.add_row([destination.name, destination.country, destination.airport_call_sign, destination.flight_time, destination.distance_from_iceland, destination.contact_name, destination.contact_phone_nr])
                
            print(table)
        
        else:
            print(UIConstants.NO_DESTINATIONS_REGISTERED)
        

    def register_destination(self):
        print(UIConstants.HEADER.format(UIConstants.REGISTER_NEW_DESTINATION))
        pass

    def find_destination(self):
        print(UIConstants.HEADER.format(UIConstants.FIND_DESTINATION))
        pass

