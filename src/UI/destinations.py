from Logic.UILogicWrapper import UI_Logic_Wrapper
from UI.Utils.Constants import UIConstants
from prettytable import PrettyTable
from Model.DestinationModel import Destination
import sys


class Destinations:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def destinations_menu_output(self):
        print(UIConstants.HEADER.format(UIConstants.MANAGE_DESTINATIONS))
        print(
            UIConstants.TWO_MENU_OPTION.format(
                UIConstants.DISPLAY_DESTINATIONS,
                UIConstants.REGISTER_NEW_DESTINATION,
                UIConstants.BACK,
                UIConstants.QUIT,
            )
        )

        # print("1. Display Destinations")
        # print("2. Register Destination")
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
                self.register_new_destination()
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
            table.field_names = [
                UIConstants.NAME,
                UIConstants.COUNTRY,
                UIConstants.AIRPORT,
                UIConstants.FLIGHT_DURATION,
                UIConstants.DISTANCE_FROM_ICELAND,
                UIConstants.CONTACT_NAME,
                UIConstants.CONTACT_PHONE_NUMBER,
            ]

            for destination in destinations:
                table.add_row(
                    [
                        destination.name,
                        destination.country,
                        destination.airport_call_sign,
                        destination.flight_time,
                        destination.distance_from_iceland,
                        destination.contact_name,
                        destination.contact_phone_nr,
                    ]
                )

            print(table)

        else:
            print(UIConstants.NO_DESTINATIONS_REGISTERED)  # Vantar fasta í constants

        print(
            UIConstants.TWO_MENU_OPTION.format(
                UIConstants.SEARCH,
                UIConstants.SORT_BY,
                UIConstants.BACK,
                UIConstants.QUIT,
            )
        )

        command = input("User Input: ")

        if command == "1" or "1.":
            pass

        elif command == "2" or "2.":
            print(
                UIConstants.FOUR_MENU_OPTION.format(
                    UIConstants.COUNTRY,
                    UIConstants.AIRPORT,
                    UIConstants.FLIGHT_DURATION,
                    UIConstants.DISTANCE_FROM_ICELAND,
                    UIConstants.BACK,
                    UIConstants.QUIT,
                )
            )

            self.get_sorted_list(input("User Input: "))
            pass

        elif command == "b" or "b.":
            pass

        elif command == "q" or "q.":
            pass

    def register_new_destination(self):
        print(UIConstants.HEADER.format(UIConstants.REGISTER_NEW_DESTINATION))
        print(UIConstants.INFORMATION_MESSAGE)

        destination_info_print = UIConstants.DESTINATION_IINFO.split(", ")
        all_destination_info = []
        for i in destination_info_print:
            print(f"{i}", end = " ")
            destination_infomation = input()
            all_destination_info.append(destination_infomation)

        name, country, airport, flight_time, distance_from_iceland, contact_name, contact_phone_nr = all_destination_info
        self.logic_wrapper.register_destination(Destination(name, country, airport, flight_time, distance_from_iceland, contact_name, contact_phone_nr))

