from UI.Utils.Constants import UIConstants
from Model.AirplaneModel import Airplane
import sys
from prettytable import PrettyTable


class Airplanes:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def airplanes_menu_output(self):
        print(UIConstants.HEADER.format(UIConstants.MANAGE_AIRPLANES))
        print(
            UIConstants.THREE_MENU_OPTION.format(
                UIConstants.DISPLAY_AIRPLANES,
                UIConstants.REGISTER_NEW_AIRPLANE,
                UIConstants.FIND_AIRPLANE,
                UIConstants.BACK,
                UIConstants.QUIT,
            )
        )

    def show_airplane_menu(self):
        self.airplanes_menu_output()
        return input("User Input: ").lower()

    def control_airplane_menu(self):
        # self.employees_menu_output()
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
            elif command == "3" or command == "3.":
                print(UIConstants.HEADER.format(UIConstants.FIND_AIRPLANE))
                self.find_airplane()
            else:
                print(UIConstants.INVALID_INPUT)
                input(UIConstants.CONTINUE_MESSAGE)

    def list_airplanes(self):  ### <=== 1. Display Airplanes
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

        # self.airplanes_menu_output()
        self.control_airplane_menu()

    def register_new_airplane(self):
        new_airplane = Airplane()
        new_airplane.insignia = input(
            "Please input the new airplanes insignia(XX-XXX). "
        )
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
