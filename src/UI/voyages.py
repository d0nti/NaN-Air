from UI.Utils.Constants import UIConstants
import sys
from prettytable import PrettyTable
from Model.VoyageModel import Voyage
from Logic.UILogicWrapper import UI_Logic_Wrapper

class Voyages:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def voyages_menu_output(self):
        # PRENTAR MENU-IÐ .  <---- PUNKTUR
        print(UIConstants.HEADER.format(UIConstants.MANAGE_VOYAGES))
        print(UIConstants.FOUR_MENU_OPTION.format(UIConstants.DISPLAY_VOYAGES, UIConstants.REGISTER_NEW_VOYAGE, UIConstants.POPULATE_VOYAGE, UIConstants.CHECK_VOYAGE_STATUS, UIConstants.BACK, UIConstants.QUIT))

        # print("1. Display Voyages")
        # print("2. Register Voyages")
        # print("3. Populate Voyage")
        # print("4. Check Voyage Status")
        # print("b. Back")
        # print("q. Quit")

    def input_prompt_voyages(self):
        # LES INPUT . <---- PUNKTUR
        # self.voyages_menu_output()
        while True:
            command = input("User Input: ")
            command = command.lower()

            if command == "q" or command == "q.":
                print(UIConstants.QUIT_MESSAGE)
                sys.exit()

            elif command == "b" or command == "b.":
                return "b"

            elif command == "1" or command == "1.":
                self.list_all_voyages()

            elif command == "2" or command == "2.":
                self.register_new_voyage()

            elif command == "3" or command == "3.":
                pass

            elif command == "4" or command == "4.":
                pass

            elif command == "5" or command == "5.":
                pass

            else:
                print(UIConstants.INVALID_INPUT)
                
                
    def list_all_voyages(self):
        voyages = self.logic_wrapper.get_all_voyages()
        
        if voyages:
            table = PrettyTable()
            table.field_names = ["Voyage ID", "Destination", "Departure Time", "Departure Date", "Arrival Time", "Arrival Date", "Captain", "Copilot", "Flight Service Manager", "Flight Attendant"]
        
            for voyage in voyages:
                table.add_row([voyage.vid, voyage.destination, voyage.departuretime, voyage.departuredate, voyage.arrivaltime, voyage.arrivaldate, voyage.captain, voyage.copilot, voyage.flight_service_manager, voyage.flight_attendant])  
            
            print(table)
        else:
            print("No voyages found.")
            
    def register_new_voyage(self):
        print("1. Register New Voyage")
        print("2. Copy Existing Voyage")
        print("3. Make Recurring Voyage")
        print("b. Back")
        print("q. Quit")
        
        command = input("User Input: ")
        
        if command == "1" or command == "1.":
            voyage_info_print = UIConstants.REGISTER_VOYAGE_INFO.split(", ")
            all_voyage_information = []
            for voyage in voyage_info_print:
                print(f"{voyage}: ", end=" ")
                voyage_information = input()
                all_voyage_information.append(voyage_information)
            print(all_voyage_information)
            
            table = PrettyTable()
            table.field_names = ["Voyage ID", "Destination", "Departure Time", "Departure Date", "Arrival Time", "Arrival Date", "Captain", "Copilot", "Flight Service Manager", "Flight Attendant"]
            
            table.add_row(all_voyage_information)
                
            print(table)
