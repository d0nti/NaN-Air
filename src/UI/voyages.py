from UI.Utils.Constants import UIConstants
import sys
from prettytable import PrettyTable
from Model.VoyageModel import Voyage
from dataclasses import asdict
from Logic.UILogicWrapper import UI_Logic_Wrapper
from datetime import datetime
from collections.abc import Iterable


def print_dataclass_as_table(instances, data_class_type):
    """Prints a dataclass as a table."""
    if not isinstance(instances, Iterable):
        instances = [instances]
    elif not instances:
        return

    table = PrettyTable(
        field_names=[field for field in data_class_type.__dataclass_fields__.keys()]
    )
    for instance in instances:
        table.add_row([v for _, v in asdict(instance).items()])

    print(table)


def print_employees_table(employees):
    """Generates a table from a list of employees."""
    table = PrettyTable(
        field_names=[
            "NID",
            "Name",
            "Role",
            "Rank",
            "Address",
            "Phone Number",
        ]
    )
    for employee in employees:
        table.add_row(
            [
                employee.nid,
                employee.name,
                employee.role,
                employee.rank,
                employee.address,
                employee.phone_nr,
            ]
        )

    print(table)


class Voyages:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def save_changes(self):
        self.logic_wrapper.write_voyages_to_disk()
        print(UIConstants.CHANGES_SAVED)
        
    def input_prompt_voyages(self):
        while True:
            print(UIConstants.HEADER.format(UIConstants.MANAGE_VOYAGES))
            print(
                UIConstants.SEVEN_MENU_OPTION.format(
                    UIConstants.DISPLAY_VOYAGES,
                    UIConstants.REGISTER_NEW_VOYAGE,
                    UIConstants.COPY_EXISTING_VOYAGE,
                    UIConstants.MAKE_RECURRING_VOYAGE,
                    UIConstants.CHOOSE_STAFF,
                    UIConstants.CHECK_VOYAGE_STATUS,
                    UIConstants.CHECK_VOYAGES_AN_EMP_IS_WORKING,
                    UIConstants.BACK,
                    UIConstants.QUIT,
                )
            )
            command = input(UIConstants.USER_INPUT).lower()

            if "q" == command:
                print(UIConstants.QUIT_MESSAGE)
                sys.exit()

            elif "b" == command:
                return "b"

            elif "1" == command:
                self.list_all_voyages()
                self.input_prompt_display_voyages()

            elif "2" == command:
                voyage_info_print = UIConstants.REGISTER_VOYAGE_INFO.split(", ")

                all_voyage_information = []
                for voyage_field in voyage_info_print:
                    print(f"{voyage_field}: ", end=" ")
                    voyage_information = input()
                    all_voyage_information.append(voyage_information)

                # Converting list to dataclass by using '*' operator that converts list to fields in dataclass
                all_voyage_information[1] = datetime.fromisoformat(
                    all_voyage_information[1]
                )
                all_voyage_information[2] = datetime.fromisoformat(
                    all_voyage_information[2]
                )
                new_voyage = Voyage(*all_voyage_information)

                print_dataclass_as_table(new_voyage, Voyage)

                self.logic_wrapper.register_new_voyage(new_voyage)
                print(UIConstants.NEW_VOYAGE_REGISTERED)
                print("Press s to save changes: ")
                command = input().lower()
                if command == "s":
                    self.save_changes()
                else:
                    continue

            elif "3" == command:
                voyage_id = input(UIConstants.ENTER_VOYAGE_ID)
                new_date = input(UIConstants.ENTER_NEW_DATE)

                self.logic_wrapper.copy_to_new_date(
                    voyage_id, datetime.fromisoformat(new_date)
                )
                print(UIConstants.VOYAGE_COPIED)
                print_dataclass_as_table(self.logic_wrapper.get_all_voyages(), Voyage)

            elif "4" == command:
                voyage_id = input(UIConstants.ENTER_VOYAGE_ID)
                interval_in_days = int(input(UIConstants.INTERVAL_DAYS))
                end_date = input(UIConstants.ENTER_END_DATE)

                self.logic_wrapper.make_recurring_voyage(
                    voyage_id, interval_in_days, datetime.fromisoformat(end_date)
                )
                print(UIConstants.VOYAGE_MADE_RECURRING)
                print_dataclass_as_table(self.logic_wrapper.get_all_voyages(), Voyage)

            elif "5" == command:
                self.populate_voyage()

            elif "6" == command:
                voyage_id = input(UIConstants.ENTER_VOYAGE_ID)
                voyage = self.logic_wrapper.find_voyage(voyage_id)
                print_dataclass_as_table(voyage, Voyage)

            # destination,departure,arrival,captain,copilot,flight_service_manager,flight_attendant,id
            elif "7" == command:
                employee_name = input("Enter employee name: ")
                filter_date = input("Enter start date to search (YYYY-MM-DD): ")

                voyages_that_an_employee_is_working = (
                    self.logic_wrapper.voyages_an_employee_is_working(
                        employee_name, filter_date
                    )
                )
                table = PrettyTable()

                table.field_names = [
                    "Destination",
                    "Departure",
                    "Arrival",
                    "Captain",
                    "Co Pilot",
                    "Flight Service Manager",
                    "Flight Attendant",
                ]

                # Add data rows to the table
                for row in voyages_that_an_employee_is_working:
                    table.add_row(
                        [
                            row["destination"],
                            row["departure"],
                            row["arrival"],
                            row["captain"],
                            row["copilot"],
                            row["flight_service_manager"],
                            row["flight_attendant"],
                        ]
                    )

                print(table)
                print(
                    f"Employee {employee_name} is working on the above voyages in the week starting on {filter_date}"
                )
            else:
                print(UIConstants.INVALID_INPUT)

    def list_all_voyages(self):
        """Lists all voyages from a file."""
        voyages = self.logic_wrapper.get_all_voyages()
        if voyages:
            print_dataclass_as_table(voyages, Voyage)
        else:
            print(UIConstants.N0_VOYAGES)

    def populate_voyage(self):
        voyage_id = input(UIConstants.ENTER_VOYAGE_ID).strip()
        while True:
            voyage = self.logic_wrapper.find_voyage(voyage_id)

            if not voyage:
                print(UIConstants.VOYAGE_NOT_FOUND)
                return

            if self.check_if_voyage_manned(voyage):
                print("Voyage is fully staffed.")
                return

            self.choose_staff_prompt(voyage)

            command = input(UIConstants.USER_INPUT)
            if "1" == command:
                captains = self.logic_wrapper.sort_by_captains()
                print_employees_table(captains)
                name = input("Input name of captain: ")
                self.logic_wrapper.set_staff(voyage_id, captain=name)
                print(f"Successfully set captain {name} to voyage {voyage.id}")
            elif "2" == command:
                copilots = self.logic_wrapper.sort_by_co_pilots()
                print_employees_table(copilots)
                name = input("Input name of copilot: ")
                self.logic_wrapper.set_staff(voyage_id, copilot=name)
                print(f"Successfully set copilot {name} to voyage {voyage.id}")
            elif "3" == command:
                managers = self.logic_wrapper.sort_by_heads_of_service()
                print_employees_table(managers)
                name = input("Input name of flight service manager: ")
                self.logic_wrapper.set_staff(voyage_id, flight_service_manager=name)
                print(
                    f"Successfully set flight service manager {name} to voyage {voyage.id}"
                )
            elif "4" == command:
                attendants = self.logic_wrapper.sort_by_flight_attendants()
                print_employees_table(attendants)
                name = input("Input name of flight attendants: ")
                self.logic_wrapper.set_staff(voyage_id, flight_attendant=name)
                print(f"Successfully set flight attendant {name} to voyage {voyage.id}")
            elif "q" == command:
                print(UIConstants.QUIT_MESSAGE)
                sys.exit()
            else:
                print(UIConstants.INVALID_INPUT)

    def check_if_voyage_manned(self, voyage):
        manned_voyages = self.logic_wrapper.get_manned_voyages()
        return voyage in manned_voyages

    def check_if_voyage_unmanned(self, voyage):
        unmanned_voyages = self.logic_wrapper.get_unmanned_voyages()
        return voyage in unmanned_voyages

    def get_unmanned_voyages(self):
        unmanned_voyages = self.logic_wrapper.get_unmanned_voyages()
        return unmanned_voyages

    def get_manned_voyages(self):
        manned_voyages = self.logic_wrapper.get_manned_voyages()
        return manned_voyages

    def input_prompt_display_voyages(self):
        while True:
            print(
                UIConstants.TWO_MENU_OPTION.format(
                    UIConstants.LIST_MANNED_VOYAGES,
                    UIConstants.LIST_UNMANNED_VOYAGES,
                    UIConstants.BACK,
                    UIConstants.QUIT,
                )
            )

            command = input(UIConstants.USER_INPUT)
            if command == "b":
                return "b"
            elif "1" == command:
                manned_voyages = self.get_manned_voyages()

                if manned_voyages:
                    print_dataclass_as_table(manned_voyages, Voyage)
                else:
                    print(UIConstants.N0_VOYAGES)
                continue

            elif "2" == command:
                unmanned_voyages = self.get_unmanned_voyages()

                if unmanned_voyages:
                    print_dataclass_as_table(unmanned_voyages, Voyage)
                else:
                    print(UIConstants.N0_VOYAGES)

                continue

            elif "q" == command:
                print(UIConstants.QUIT_MESSAGE)
                sys.exit()

    def choose_staff_prompt(self, voyage):
        print("Voyage not fully staffed.")

        if not voyage.captain:
            print("1. Add Captain")
        if not voyage.copilot:
            print("2. Add Co-Pilot")
        if not voyage.flight_service_manager:
            print("3. Add Head of Service")
        if not voyage.flight_attendant:
            print("4. Add Flight Attendant")
        else:
            print("Voyage is fully staffed.")
        print(UIConstants.QUIT)
