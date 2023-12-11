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
        print(
            UIConstants.FOUR_MENU_OPTION.format(
                UIConstants.DISPLAY_VOYAGES,  # 1. Display Voyages
                UIConstants.REGISTER_NEW_VOYAGE,  # 2. Register Voyages
                UIConstants.POPULATE_VOYAGE,  # 3. Populate Voyage
                UIConstants.CHECK_VOYAGE_STATUS,  # 4. Check Voyage Status
                UIConstants.BACK,  # b. Back
                UIConstants.QUIT,  # q. Quit
            )
        )

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
                self.populate_voyage()

            elif command == "4" or command == "4.":
                filter = input("Enter Voyage ID or Destination: ")
                self.search_voyages(filter)

            else:
                print(UIConstants.INVALID_INPUT)

    def list_all_voyages(self):
        voyages = self.logic_wrapper.get_all_voyages()

        if voyages:
            table = PrettyTable()
            table.field_names = [
                "Voyage ID",
                "Destination",
                "Departure Time",
                "Departure Date",
                "Arrival Time",
                "Arrival Date",
                "Captain",
                "Copilot",
                "Flight Service Manager",
                "Flight Attendant",
            ]

            for voyage in voyages:
                table.add_row(
                    [
                        voyage.vid,
                        voyage.destination,
                        voyage.departuretime,
                        voyage.departuredate,
                        voyage.arrivaltime,
                        voyage.arrivaldate,
                        voyage.captain,
                        voyage.copilot,
                        voyage.flight_service_manager,
                        voyage.flight_attendant,
                    ]
                )

            print(table)
        else:
            print("No voyages found.")

    def register_new_voyage(self):
        # voyages = self.logic_wrapper.get_all_voyages()

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

            table = PrettyTable()
            table.field_names = [
                "Voyage ID",
                "Destination",
                "Departure Time",
                "Departure Date",
                "Arrival Time",
                "Arrival Date",
                "Captain",
                "Copilot",
                "Flight Service Manager",
                "Flight Attendant",
            ]

            table.add_row(all_voyage_information)

            print(table)

            self.logic_wrapper.register_new_voyage(all_voyage_information)

            print("New Voyage Registered.")
        elif command == "2" or command == "2.":
            self.copy_existing_voyage()
            
        elif command == "b":
            return "b"
            
        elif command == "q":
            print(UIConstants.QUIT_MESSAGE)
            sys.exit()

    def populate_voyage(self):
        voyages = self.logic_wrapper.get_all_voyages()
        for voyage in voyages:
            if voyage.captain == "None":
                sorted_captains = self.logic_wrapper.sort_by_captains()
                table = PrettyTable()
                table.field_names = [
                    "NID",
                    "Name",
                    "Role",
                    "Rank",
                    "Address",
                    "Phone Number",
                    "License",
                ]
                for captain in sorted_captains:
                    table.add_row(
                        [
                            captain.nid,
                            captain.name,
                            captain.role,
                            captain.rank,
                            captain.address,
                            captain.phone_nr,
                            captain.license,
                        ]
                    )

                print(
                    voyage.vid,
                    voyage.destination,
                    voyage.departuretime,
                    voyage.departuredate,
                    voyage.arrivaltime,
                    voyage.arrivaldate,
                )
                print("Available Captains: ")
                print(table)
            elif voyage.copilot == "None":
                sorted_copilots = self.logic_wrapper.sort_by_co_pilots()
                table = PrettyTable()
                table.field_names = [
                    "NID",
                    "Name",
                    "Role",
                    "Rank",
                    "Address",
                    "Phone Number",
                    "License",
                ]
                for copilot in sorted_copilots:
                    table.add_row(
                        [
                            copilot.nid,
                            copilot.name,
                            copilot.role,
                            copilot.rank,
                            copilot.address,
                            copilot.phone_nr,
                            copilot.license,
                        ]
                    )

                print(
                    voyage.vid,
                    voyage.destination,
                    voyage.departuretime,
                    voyage.departuredate,
                    voyage.arrivaltime,
                    voyage.arrivaldate,
                )
                print("Available Copilots: ")
                print(table)
            elif voyage.flight_service_manager == "None":
                sorted_heads_of_service = self.logic_wrapper.sort_by_heads_of_service()
                table = PrettyTable()
                table.field_names = [
                    "NID",
                    "Name",
                    "Role",
                    "Rank",
                    "Address",
                    "Phone Number",
                ]
                for head_of_service in sorted_heads_of_service:
                    table.add_row(
                        [
                            head_of_service.nid,
                            head_of_service.name,
                            head_of_service.role,
                            head_of_service.rank,
                            head_of_service.address,
                            head_of_service.phone_nr,
                        ]
                    )

                print(
                    voyage.vid,
                    voyage.destination,
                    voyage.departuretime,
                    voyage.departuredate,
                    voyage.arrivaltime,
                    voyage.arrivaldate,
                )
                print("Available Heads of Service: ")
                print(table)
            elif voyage.flight_attendant == "None":
                sorted_flight_attendants = (
                    self.logic_wrapper.sort_by_flight_attendants()
                )
                table = PrettyTable()
                table.field_names = [
                    "NID",
                    "Name",
                    "Role",
                    "Rank",
                    "Address",
                    "Phone Number",
                ]
                for flight_attendant in sorted_flight_attendants:
                    table.add_row(
                        [
                            flight_attendant.nid,
                            flight_attendant.name,
                            flight_attendant.role,
                            flight_attendant.rank,
                            flight_attendant.address,
                            flight_attendant.phone_nr,
                        ]
                    )

                print(
                    voyage.vid,
                    voyage.destination,
                    voyage.departuretime,
                    voyage.departuredate,
                    voyage.arrivaltime,
                    voyage.arrivaldate,
                )
                print("Available Flight Attendants: ")
                print(table)
            else:
                print("All registered voyages are fully staffed.")

    def search_voyages(self, filter):
        #filter = input("Enter Voyage ID or Destination: ") - from input_prompt_voyages
        filtered_voyages = self.logic_wrapper.search_voyages(filter)
        table = PrettyTable()
        
        table.field_names = [
            "Voyage ID",
            "Destination",
            "Departure Time",
            "Departure Date",
            "Arrival Time",
            "Arrival Date",
            "Captain",
            "Copilot",
            "Flight Service Manager",
            "Flight Attendant",
        ]
        
        for voyage in filtered_voyages:
            table.add_row(
                [
                    voyage.get('vid'),
                    voyage.get('destination'),
                    voyage.get('departuretime'),
                    voyage.get('departuredate'),
                    voyage.get('arrivaltime'),
                    voyage.get('arrivaldate'),
                    voyage.get('captain'),
                    voyage.get('copilot'),
                    voyage.get('flight_service_manager'),
                    voyage.get('flight_attendant'),
                ]
            )
        
        print(table)

    def copy_existing_voyage(self):
        
        voyage = self.logic_wrapper.search_voyages(input("Enter Voyage ID or Destination: "))
        
        if voyage:
            self.logic_wrapper.register_new_voyage(voyage)
            print("Voyage Copied.")
        else:
            print("No voyage found.")
            
        # Eftir að klára :-) :-(

    def make_recurring_voyage(self):
        pass
    
    def edit_voyage(self):
        pass