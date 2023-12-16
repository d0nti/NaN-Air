from UI.Utils.Constants import UIConstants
from Model.AirplaneModel import Airplane
from Logic.Verifications.verifyairplane import(
InsigniaExistsError, InsigniaFormatError, InvalidInsigniaCharacterError
)
from prettytable import PrettyTable
import sys


class Airplanes:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def airplanes_menu_output(self):
        """ Prints the main menu of the airplane management environment,
        showing that the user can access a list of all Airplanes and
        register a new airplane from this point in the program
        """
        print(UIConstants.HEADER.format(UIConstants.MANAGE_AIRPLANES))
        print(
            UIConstants.TWO_MENU_OPTION.format(
                UIConstants.DISPLAY_AIRPLANES,
                UIConstants.REGISTER_NEW_AIRPLANE,
                UIConstants.BACK,
                UIConstants.QUIT,
            )
        )

    def show_airplane_menu(self):
        """This function calls the main menu for the airplane management environment"""
        self.airplanes_menu_output()
        return input("User Input: ").lower()

    def control_airplane_menu(self):
        """This function controls the main menu for the airplane management environment"""
        while (command := self.show_airplane_menu()) not in ("b", "b."):
            if command == "q" or command == "q.":
                print(UIConstants.QUIT_MESSAGE)
                sys.exit()
            elif command == "1" or command == "1.":
                print(UIConstants.HEADER.format(UIConstants.DISPLAY_AIRPLANES))
                self.list_airplanes()
            elif command == "2" or command == "2.":
                print(UIConstants.HEADER.format(UIConstants.REGISTER_NEW_AIRPLANE))
                self.register_new_airplane()
            else:
                print(UIConstants.INVALID_INPUT)


    def list_airplanes(self):
        """This function gets and prints all airplanes"""
        airplanes = self.logic_wrapper.get_all_airplanes()

        if airplanes:
            table = PrettyTable()
            table.field_names = [
                UIConstants.NAME,
                UIConstants.TYPE,
                UIConstants.SUPPLIER,
                UIConstants.SEATS,
            ]

            for airplane in airplanes:
                table.add_row(
                    [
                        airplane.insignia,
                        airplane.plane_type,
                        airplane.supplier,
                        airplane.seats,
                    ]
                )

            print(table)

    def register_new_airplane(self):
        """This function registers new airplanes"""
        is_new_airplane_valid = False
        while not is_new_airplane_valid:
            try:
                new_airplane = Airplane()
                new_airplane.insignia = input(
                    "Please input the new airplanes insignia(XX-XXX). "
                )
                if new_airplane.insignia != "":

                    plane_type = input(
                        "Choose an airplane type for the new aircraft.\n1. BAE146 \n2. FokkerF28 \n3. FokkerF100\n"
                    )
                    if plane_type == "1" or plane_type == "1.":
                        new_airplane.plane_type = "NABAE146"
                    if plane_type == "2" or plane_type == "2.":
                        new_airplane.plane_type = "NAFokkerF28"
                    if plane_type == "3" or plane_type == "3.":
                        new_airplane.plane_type = "NAFokkerF100"
                    self.logic_wrapper.register_airplane(new_airplane)
                else:
                    print(UIConstants.INVALID_INPUT)
                    break
               

            except InvalidInsigniaCharacterError:
                print(UIConstants.AIRPLANE_INVALID_INSIGNIA_CHARACTER_ERROR)

            except InsigniaFormatError:
                print(UIConstants.AIRPLANE_INSIGNIA_FORMAT_ERROR)

            except InsigniaExistsError:
                print(UIConstants.AIRPLANE_INSIGNIA_EXISTS_ERROR)

            else:
                print(UIConstants.SUCCESSFULL_REGISTRATION_FOR_AIRPLANE)
                is_new_airplane_valid = True

    def find_airplane(self):
        filter = input(UIConstants.PLANE_SEARCH_PARAM)
        filtered_airplane = self.logic_wrapper.search_airplane(filter)
        self.__print_airplane(filtered_airplane)

    def __print_airplane(self, filtered_airplane):
        table = PrettyTable()
        table.field_names = [
            UIConstants.PLANE_INSIGNIA,
            UIConstants.PLANE_TYPE_ID,
        ]

        for airplane in filtered_airplane:
            table.add_row(
                [
                    airplane.insignia,
                    airplane.plane_type,
                ]
            )
        print(table)
