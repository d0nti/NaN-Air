from UI.Utils.Constants import UIConstants
import sys
from prettytable import PrettyTable
from Model.VoyageModel import Voyage
from Model.EmployeeModel import Employee, Pilot, FlightAttendant
from dataclasses import fields, asdict
from Logic.UILogicWrapper import UI_Logic_Wrapper
from datetime import datetime
from collections.abc import Iterable


def print_dataclass_as_table(instances, data_class_type):
    """Prints a dataclass as a table."""
    if not isinstance(instances, Iterable):
        instances = [instances]

    table = PrettyTable(
        field_names=[field for field in data_class_type.__dataclass_fields__.keys()]
    )
    if not instances:
        return
    for instance in instances:
        table.add_row([v for _, v in asdict(instance).items()])

    print(table)


def generate_table(employees):
    """Generates a table from a list of employees."""
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

    for employee in employees:
        table.add_row(
            [
                employee.nid,
                employee.name,
                employee.role,
                employee.rank,
                employee.address,
                employee.phone_nr,
                employee.license,
            ]
        )

    return table


class Voyages:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def voyages_menu_output(self):
        # * PRENTAR MENU-IÐ .  <---- PUNKTUR
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
        )+

    def input_prompt_voyages(self):
        # *LES INPUT . <---- PUNKTUR
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
                print("1. List manned voyages")
                print("2. List unmanned voyages")
                print("b. Back")
                print("q. Quit")

                """ÞARF AÐ KLÁRA HÉR MANNED OG UNMANNED VOYAGES"""

                if command == "1" or command == "1.":
                    manned_voyages = self.logic_wrapper.get_manned_voyages()
                    print_dataclass_as_table(manned_voyages, Voyage)

                elif command == "2" or command == "2.":
                    unmanned_voyages = self.logic_wrapper.get_unmanned_voyages()
                    print_dataclass_as_table(unmanned_voyages, Voyage)

                elif command == "b" or command == "b.":
                    return "b"

                elif command == "q" or command == "q.":
                    print(UIConstants.QUIT_MESSAGE)
                    sys.exit()

            elif command == "2" or command == "2.":
                self.register_new_voyage()

            elif command == "3" or command == "3.":
                self.populate_voyage()

            elif command == "4" or command == "4.":
                voyage_id = input("Enter Voyage ID: ")
                voyage = self.logic_wrapper.find_voyage(voyage_id)
                print_dataclass_as_table(voyage, Voyage)

            else:
                print(UIConstants.INVALID_INPUT)

    def list_all_voyages(self):
        """Lists all voyages from a file."""
        voyages = self.logic_wrapper.get_all_voyages()

        if voyages:
            print_dataclass_as_table(voyages, Voyage)
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

            table = PrettyTable(UIConstants.REGISTER_VOYAGE_INFO.split(", "))
            table.add_row(all_voyage_information)
            print(table)

            self.logic_wrapper.register_new_voyage(all_voyage_information)
            print("New Voyage Registered.")

        elif command == "2" or command == "2.":
            voyage_id = input("Enter Voyage ID: ")
            new_date = input("Enter new date (YYYY-MM-DD): ")

            self.logic_wrapper.copy_to_new_date(
                voyage_id, datetime.fromisoformat(new_date)
            )
            print("Voyage copied.")
            print_dataclass_as_table(self.logic_wrapper.get_all_voyages(), Voyage)

        elif command == "3" or command == "3.":
            voyage_id = input("Enter Voyage ID: ")
            interval_in_days = int(input("Enter interval in days: "))
            end_date = input("Enter end date (YYYY-MM-DD): ")

            self.logic_wrapper.make_recurring_voyage(
                voyage_id, interval_in_days, datetime.fromisoformat(end_date)
            )
            print("Voyage made recurring.")
            print_dataclass_as_table(self.logic_wrapper.get_all_voyages(), Voyage)

        elif command == "b":
            return "b"

        elif command == "q":
            print(UIConstants.QUIT_MESSAGE)
            sys.exit()

    def populate_voyage(self):
        voyages = self.logic_wrapper.get_all_voyages()
        for voyage in voyages:
            if voyage.captain == "None" or voyage.captain == "":
                sorted_captains = self.logic_wrapper.sort_by_captains()
                table = generate_table(sorted_captains)

                print(
                    f"Voyage ID: {voyage.id}, {voyage.destination}, {voyage.departure}, {voyage.arrival}"
                )
                print("Available Captains: ")
                print(table)

            elif voyage.copilot == "None" or voyage.copilot == "":
                sorted_copilots = self.logic_wrapper.sort_by_co_pilots()
                table = generate_table(sorted_copilots)

                print(
                    f"Voyage ID: {voyage.id}, {voyage.destination}, {voyage.departure}, {voyage.arrival}"
                )
                print("Available Copilots: ")
                print(table)

            elif (
                voyage.flight_service_manager == "None"
                or voyage.flight_service_manager == ""
            ):
                sorted_heads_of_service = self.logic_wrapper.sort_by_heads_of_service()
                table = generate_table(sorted_heads_of_service)

                print(
                    f"Voyage ID: {voyage.id}, {voyage.destination}, {voyage.departure}, {voyage.arrival}"
                )
                print("Available Heads of Service: ")
                print(table)

            elif voyage.flight_attendant == "None" or voyage.flight_attendant == "":
                sorted_flight_attendants = (
                    self.logic_wrapper.sort_by_flight_attendants()
                )
                table = generate_table(sorted_flight_attendants)

                print(
                    f"Voyage ID: {voyage.id}, {voyage.destination}, {voyage.departure}, {voyage.arrival}"
                )
                print("Available Flight Attendants: ")
                print(table)

            else:
                print(
                    f"Voyage {voyage.destination} {voyage.departure}, ({voyage.id}) is fully staffed."
                )

    def get_manned_voyages(self):
        manned_voyages = self.logic_wrapper.get_manned_voyages()
        print_dataclass_as_table(manned_voyages, Voyage)
        return manned_voyages

    def get_unmanned_voyages(self):
        unmanned_voyages = self.logic_wrapper.get_unmanned_voyages()
        print_dataclass_as_table(unmanned_voyages, Voyage)
        return unmanned_voyages
