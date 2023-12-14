from UI.Utils.Constants import UIConstants
from Model.AirplaneModel import Airplane
import sys
from prettytable import PrettyTable


class Airplanes:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def airplanes_menu_output(self):
        print(UIConstants.HEADER.format(UIConstants.MANAGE_AIRPLANES))
        print(UIConstants.FOUR_MENU_OPTION.format(UIConstants.DISPLAY_AIRPLANES, UIConstants.REGISTER_NEW_AIRPLANE, UIConstants.FIND_AIRPLANE, UIConstants.PRINT_AIRPLANE_EFFICIENCY, UIConstants.BACK, UIConstants.QUIT))
        
        # print("1. Display Airplane")
        # print("2. Register New Airplane")
        # print("3. Find Airplane")
        # print("4. Print Airplane Efficiency")
        # print("b. Back")
        # print("q. Quit")

    def input_prompt_airplanes(self):
        while True:
            command = input("User Input: ")
            command = command.lower()

            if command == "q" or command == "q.":
                print(UIConstants.QUIT_MESSAGE)
                sys.exit()

            elif command == "b" or command == "b.":
                return "b"
                

            elif command == "1" or command == "1.":
                self.list_airplanes()

            
            elif command == "2" or command == "2.":
                self.register_new_airplane()

            elif command == "3" or command == "3.":
                self.find_airplane()

            elif command == "4" or command == "4.":
                self.print_airplane_efficiency()

            else:
                print(UIConstants.INVALID_INPUT)
                

    def list_airplanes(self): ### <=== 1. Display Airplanes
        print(UIConstants.HEADER.format(UIConstants.DISPLAY_AIRPLANES))
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


        self.airplanes_menu_output()
        self.input_prompt_airplanes()
    
    def register_new_airplane(self):
        print(UIConstants.HEADER.format(UIConstants.REGISTER_NEW_AIRPLANE))
        new_airplane = Airplane()
        new_airplane.insignia = input("Please input the new airplanes insignia(XX-XXX). ")
        plane_type = input("Choose an airplane type for the new aircraft.\n1. BAE146 \n2. FokkerF28 \n3. FokkerF100\n")
        if plane_type == "1" or plane_type == "1.":
            new_airplane.plane_type = "NABAE146"
        if plane_type == "2" or plane_type == "2.":
            new_airplane.plane_type = "NAFokkerF28"
        if plane_type == "3" or plane_type == "3.":
            new_airplane.plane_type = "NAFokkerF100"
        self.logic_wrapper.register_airplane(new_airplane)

    def find_airplane(self):
        print(UIConstants.HEADER.format(UIConstants.FIND_AIRPLANE))
        pass

    def print_airplane_efficiency(self):
        print(UIConstants.HEADER.format(UIConstants.PRINT_AIRPLANE_EFFICIENCY))
        pass