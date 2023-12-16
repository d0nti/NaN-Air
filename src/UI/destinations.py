from UI.Utils.Constants import UIConstants
from prettytable import PrettyTable
from Model.DestinationModel import Destination
from Logic.Verifications.verifydestination import (
    DestinationNameError,
    DestinationNameExistsError,
    DestinationCountryError,
    DestinationAirportError,
    DestinationAirportExistsError,
    DestinationDistanceError,
    DestinationFlightTimeError,
    DestinationContactError,
    DestinationContactNumberError,
    DestinationContactNumberExistsError,
    DestinationContactNumberLenghtError,
)
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

    def show_destination_menu(self):
        self.destinations_menu_output()
        return input("User Input: ").lower()

    def control_destination_menu(self):
        while (command := self.show_destination_menu()) not in ("b", "b."):
            if command == "q" or command == "q.":
                print(UIConstants.QUIT_MESSAGE)
                sys.exit()
            elif command == "1" or command == "1.":
                print(UIConstants.HEADER.format(UIConstants.DISPLAY_DESTINATIONS))
                self.list_destinations()

            elif command == "2" or command == "2.":
                print(UIConstants.HEADER.format(UIConstants.REGISTER_NEW_DESTINATION))
                self.register_new_destination()

            elif command == "3" or command == "3.":
                print(UIConstants.HEADER.format(UIConstants.FIND_DESTINATION))
                self.find_destination()

            elif command == "4" or command == "4.":
                print(UIConstants.HEADER.format(UIConstants.UPDATE_DESTINATION))
                self.update_destination()
            else:
                print(UIConstants.INVALID_INPUT)
                input(UIConstants.CONTINUE_MESSAGE)

    def list_destinations(self):
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
                        destination.airport + "_Airport",
                        destination.flight_time + "_hour",
                        destination.distance_from_Iceland + "km",
                        destination.contact_name,
                        destination.contact_phone_nr,
                    ]
                )

            print(table)

        else:
            print(UIConstants.NO_DESTINATIONS_REGISTERED)

    def register_new_destination(self):
        print(UIConstants.INFORMATION_MESSAGE)

        destination_info_print = UIConstants.DESTINATION_INFO.split(", ")

        is_destination_valid = False
        while not is_destination_valid:
            all_destination_info = []
            try:
                for i in destination_info_print:
                    # all_destination_info = []
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
                print(UIConstants.SUCCESSFULL_REGISTRATION_FOR_DESTINATION)
                is_destination_valid = True

    def find_destination(self):
        print(
            f"{UIConstants.SEARCH_DESTINATION_MESSAGE} \n {UIConstants.SEARCH_DESTINATION_MESSAGE_CONTINUE}"
        )

        while (command := input("\nUser Input (press enter to go back): ")).lower():
            try:
                destinations = self.logic_wrapper.search_destination(command)
                self.__print_destination(destinations)

            except DestinationSearchFilterNotFoundError:
                print(UIConstants.INVALID_INPUT)
                print(UIConstants.DESTINATION_SEARCH_FILTER_NOT_FOUND_ERROR_MESSAGE)

    def __print_destination(self, destinations):
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
                    destination.airport + "_Airport",
                    destination.flight_time + "_hour",
                    destination.distance_from_Iceland + "km",
                    destination.contact_name,
                    destination.contact_phone_nr,
                ]
            )

        print(table)

    def update_destination(self):
        print(UIConstants.UPDATE_DESTINATION_MESSAGE)

        correct_destination_name = False
        destination_to_change = ""
        while correct_destination_name == False:
            destination_to_change = input(
                "\nUser Input (press enter to go back): "
            ).lower()
            if self.logic_wrapper.search_destination(destination_to_change):
                destination_to_change = self.logic_wrapper.search_destination(
                    destination_to_change
                )[0]
            if destination_to_change:
                correct_destination_name = True
            else:
                print(
                    "You have entered a destination that does not exist, please try again "
                )
                pass

            destination_info_prints = UIConstants.UPDATE_DESTINATION_INFO.split(", ")
            all_destination_information = []

            for info in destination_info_prints:
                print(f"{info}", end=" ")
                new_information = input()
                all_destination_information.append(new_information)

            contact_name, contact_phone_nr = all_destination_information

            self.logic_wrapper.update_destination(
                Destination(destination_to_change), all_destination_information
            )


"""                is_update_valid = False

                while not is_update_valid:
                    try:
                        self.logic_wrapper.update_destination(
                            destination_to_change, 
                        )
                    except DestinationContactError:
                        print(UIConstants.DESTINATION_CONTACT_ERROR_MESSAGE)

                    except DestinationContactNumberError:
                        print(UIConstants.DESTINATION_CONTACT_NUMBER_ERROR_MESSAGE)

                    except DestinationContactNumberLenghtError:
                        print(UIConstants.DESTINATION_CONTACT_NUMBER_ERROR_MESSAGE)

                    except DestinationContactNumberExistsError:
                        print(
                            UIConstants.DESTINATION_CONTACT_NUMBER_EXISTS_ERROR_MESSAGE
                        )

                    else:
                        print(UIConstants.SUCCESSFULL_UPDATE_FOR_DESTINATION)
                        is_update_valid = True
"""
