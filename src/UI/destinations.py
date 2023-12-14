from UI.Utils.Constants import UIConstants
from prettytable import PrettyTable
from Model.DestinationModel import Destination
from Logic.Verifications.verifydestination import(
DestinationNameError,DestinationNameExistsError,DestinationCountryError,
DestinationCountryExistsError,DestinationAirportError,DestinationAirportExistsError,
DestinationDistanceError,DestinationFlightTimeError,DestinationContactError,DestinationContactNumberError,
DestinationContactNumberExistsError,DestinationContactNumberLenghtError)
from Logic.destinationlogic import DestinationSearchFilterNotFoundError
import sys


class Destinations:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def destinations_menu_output(self):
        print(UIConstants.HEADER.format(UIConstants.MANAGE_DESTINATIONS))
        print(
            UIConstants.FOUR_MENU_OPTION.format(
                UIConstants.DISPLAY_DESTINATIONS,
                UIConstants.REGISTER_NEW_DESTINATION,
                UIConstants.FIND_DESTINATION,
                UIConstants.UPDATE_DESTINATION,
                UIConstants.BACK,
                UIConstants.QUIT,
            )
        )

        # print("1. Display Destinations")
        # print("2. Register Destination")
        # print("3. Find Destination")
        # print("3. Update Destination")
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
                back = self.list_destinations() #<==== DISPLAY DESTINATIONS
                if back == "b":
                    pass
            elif command == "2" or command == "2.":
                self.register_new_destination()

            elif command == "3" or command == "3.":
                self.find_destination()

            elif command == "4" or command == "4.":
                self.update_destination()

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
                        destination.airport,
                        destination.flight_time + "_hour",
                        destination.distance_from_Iceland + "km",
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
            print("Destination go BACK!")
            self.destinations_menu_output()
            self.input_prompt_destinations()
            return "b"


        elif command == "q" or "q.":
            pass

    def register_new_destination(self):
        print(UIConstants.HEADER.format(UIConstants.REGISTER_NEW_DESTINATION))
        print(UIConstants.INFORMATION_MESSAGE)

        destination_info_print = UIConstants.DESTINATION_INFO.split(", ")
        all_destination_info = []

        is_destination_valid = False
        while not is_destination_valid:
            try:
                for i in destination_info_print:
                    print(f"{i}", end=" ")
                    destination_infomation = input()
                    all_destination_info.append(destination_infomation)

                (
                    name,
                    country,
                    airport,
                    flight_time,
                    distance_from_Iceland,
                    contact_name,
                    contact_phone_nr,
                ) = all_destination_info

                self.logic_wrapper.register_destination(
                    Destination(
                        name,
                        country,
                        airport,
                        flight_time,
                        distance_from_Iceland,
                        contact_name,
                        contact_phone_nr,
                    )
                )

            except DestinationNameError:
                print(UIConstants.DESTINATION_NAME_ERROR_MESSAGE)

            except DestinationNameExistsError:
                print(UIConstants.DESTINATION_NAME_EXISTS_ERROR_MESSAGE)

            except DestinationCountryError:
                print(UIConstants.DESTINATION_COUNTRY_ERROR_MESSAGE)

            except DestinationAirportError:
                print(UIConstants.DESTINATION_AIRPORT_ERROR_MESSAGE)

            except DestinationAirportExistsError:
                print(UIConstants.DESTINATION_AIRPORT_EXISTS_ERROR_MESSAGE)

            except DestinationDistanceError:
                print(UIConstants.DESTINATION_DISTANCE_ERROR_MESSAGE)

            except DestinationFlightTimeError:
                print(UIConstants.DESTINATION_FLIGHT_TIME_ERROR_MESSAGE)

            except DestinationContactError:
                print(UIConstants.DESTINATION_CONTACT_ERROR_MESSAGE)

            except DestinationContactNumberError:
                print(UIConstants.DESTINATION_CONTACT_NUMBER_ERROR_MESSAGE)

            except DestinationContactNumberExistsError:
                print(UIConstants.DESTINATION_CONTACT_NUMBER_EXISTS_ERROR_MESSAGE)

            except DestinationContactNumberLenghtError:
                print(UIConstants.DESTINATION_CONTACT_NUMBER_ERROR_MESSAGE)

            else:
                print(UIConstants.SUCCESFULL_REGISTRATION_FOR_DESTINATION)
                is_destination_valid = True

    def find_destination(self):
        print(UIConstants.HEADER.format(UIConstants.FIND_DESTINATION))
        print(UIConstants.SEARCH_DESTINATION_MESSAGE)

        is_search_destination_valid = False
        while not is_search_destination_valid:
            try:
                print()
                command = input("User Input: ")
                searched_destination = self.logic_wrapper.search_destination(command)

                if searched_destination:
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

                    for destination in searched_destination:
                        table.add_row(
                            [
                                destination.name,
                                destination.country,
                                destination.airport,
                                destination.flight_time + "_hour",
                                destination.distance_from_Iceland + "km",
                                destination.contact_name,
                                destination.contact_phone_nr,
                            ]
                        )

                    print(table)
            except DestinationSearchFilterNotFoundError:
                print(UIConstants.INVALID_INPUT)
                print(UIConstants.DESTINATION_SEARCH_FILTER_NOT_FOUND_ERROR_MESSAGE)

            else:
                is_search_destination_valid = True

    def update_destination(self):
        print(UIConstants.HEADER.format(UIConstants.UPDATE_DESTINATION))
        print(UIConstants.UPDATE_DESTINATION_MESSAGE)

        destination_name = input("User Input: ")
        destination = self.logic_wrapper.search_destination(destination_name)

        if destination:
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

            table.add_row(
                [
                    destination.name,
                    destination.country,
                    destination.airport,
                    destination.flight_time + "_hour",
                    destination.distance_from_Iceland + "km",
                    destination.contact_name,
                    destination.contact_phone_nr,
                ]
            )

            print(table)
            print(UIConstants.INFORMATION_MESSAGE)

        all_info_to_change = []
        for change_info in UIConstants.UPDATE_DESTINATION_INFO.split(", "):
            print(f"{change_info}", end=" ")
            changed_info = input()
            all_info_to_change.append(changed_info)
        contact_name, contact_phone_nr = all_info_to_change

        is_update_valid = False
        while not is_update_valid:
            try:
                self.logic_wrapper.update_destination(
                    destination, contact_name, contact_phone_nr
                )
            except DestinationContactError:
                print(UIConstants.DESTINATION_CONTACT_ERROR_MESSAGE)

            except DestinationContactNumberError:
                print(UIConstants.DESTINATION_CONTACT_NUMBER_ERROR_MESSAGE)

            except DestinationContactNumberLenghtError:
                print(UIConstants.DESTINATION_CONTACT_NUMBER_ERROR_MESSAGE)

            except DestinationContactNumberExistsError:
                print(UIConstants.DESTINATION_CONTACT_NUMBER_EXISTS_ERROR_MESSAGE)

            else:
                print(UIConstants.SUCCESFULL_UPDATE_FOR_DESTINATION)
                is_update_valid = True
