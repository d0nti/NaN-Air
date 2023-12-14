from UI.Utils.Constants import UIConstants
import sys
from prettytable import PrettyTable
from Model.VoyageModel import Voyage
from Model.EmployeeModel import Employee, Pilot, FlightAttendant
from dataclasses import fields, asdict, replace
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

    def save_and_quit(self):
        self.logic_wrapper.write_voyages_to_disk()
        print(UIConstants.QUIT_MESSAGE)
        sys.exit()

    def input_prompt_voyages(self):
        while True:
            print(UIConstants.HEADER.format(UIConstants.MANAGE_VOYAGES))
            print("1. Display Voyages")
            print("2. Register New Voyage")
            print("3. Copy Existing Voyage")
            print("4. Make Recurring Voyage")
            print("5. Choose Staff")
            print("6. Check Voyage Status")
            print("7. Check Voyages an Employee is Working")
            print("q. Quit")
            command = input("User Input: ").lower()

            if "q" in command:
                self.save_and_quit()

            elif "b" in command:
                return "b"

            elif "1" in command:
                self.list_all_voyages()
                self.input_prompt_display_voyages()

            elif "2" in command:
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

            elif "3" in command:
                voyage_id = input("Enter Voyage ID: ")
                new_date = input("Enter new date (YYYY-MM-DD): ")

                self.logic_wrapper.copy_to_new_date(
                    voyage_id, datetime.fromisoformat(new_date)
                )
                print("Voyage copied.")
                print_dataclass_as_table(self.logic_wrapper.get_all_voyages(), Voyage)

            elif "4" in command:
                voyage_id = input("Enter Voyage ID: ")
                interval_in_days = int(input("Enter interval in days: "))
                end_date = input("Enter end date (YYYY-MM-DD): ")

                self.logic_wrapper.make_recurring_voyage(
                    voyage_id, interval_in_days, datetime.fromisoformat(end_date)
                )
                print("Voyage made recurring.")
                print_dataclass_as_table(self.logic_wrapper.get_all_voyages(), Voyage)

            elif "5" in command:
                self.populate_voyage()

            elif "6" in command:
                voyage_id = input("Enter Voyage ID: ")
                voyage = self.logic_wrapper.find_voyage(voyage_id)
                print_dataclass_as_table(voyage, Voyage)
            
            #destination,departure,arrival,captain,copilot,flight_service_manager,flight_attendant,id
            elif "7" in command:
                employee_name = input("Enter employee name: ")
                filter_date = input("Enter date (YYYY-MM-DD): ")

                voyages_that_an_employee_is_working = self.logic_wrapper.voyages_an_employee_is_working(employee_name, filter_date)
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
                    table.add_row([
                        row['destination'],
                        row['departure'],
                        row['arrival'],
                        row['captain'],
                        row['copilot'],
                        row['flight_service_manager'],
                        row['flight_attendant']
                    ])

                # Print the table
                print(table)
                print(f"Employee {employee_name} is working on the above voyages in the week starting on {filter_date}")
            else:
                print(UIConstants.INVALID_INPUT)

    def list_all_voyages(self):
        """Lists all voyages from a file."""
        voyages = self.logic_wrapper.get_all_voyages()

        if voyages:
            print_dataclass_as_table(voyages, Voyage)
        else:
            print("No voyages found.")

    def populate_voyage(self):
        voyage_id = input("Enter Voyage ID: ").strip()
        while True:
            voyage = self.logic_wrapper.find_voyage(voyage_id)

            if not voyage:
                print("Voyage not found")
                return

            if self.check_if_voyage_manned(voyage):
                print("Voyage is fully staffed.")
                return

            self.choose_staff_prompt(voyage)

            command = input("User Input: ")
            if "1" in command:
                captains = self.logic_wrapper.sort_by_captains()
                print_employees_table(captains)
                nid = input("Select nid (National ID) of captain: ")
                self.logic_wrapper.set_staff(voyage_id, captain=nid)
                print(f"Successfully set captain {nid} to voyage {voyage.id}")
            elif "2" in command:
                copilots = self.logic_wrapper.sort_by_co_pilots()
                print_employees_table(copilots)
                nid = input("Select nid (National ID) of copilot: ")
                self.logic_wrapper.set_staff(voyage_id, copilot=nid)
                print(f"Successfully set copilot {nid} to voyage {voyage.id}")
            elif "3" in command:
                managers = self.logic_wrapper.sort_by_heads_of_service()
                print_employees_table(managers)
                nid = input("Select nid (National ID) of flight service manager: ")
                self.logic_wrapper.set_staff(voyage_id, flight_service_manager=nid)
                print(
                    f"Successfully set flight service manager {nid} to voyage {voyage.id}"
                )
            elif "4" in command:
                attendants = self.logic_wrapper.sort_by_flight_attendants()
                print_employees_table(attendants)
                nid = input("Select nid (National ID) of flight attendants: ")
                self.logic_wrapper.set_staff(voyage_id, flight_attendant=nid)
                print(
                    f"Successfully set flight attendant {nid} to voyage {voyage.id}"
                )
            elif "q" in command:
                self.save_and_quit()
            else:
                print("Invalid input, try again...")

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
            print("1. List Manned Voyages" )
            print("2. List Unmanned Voyages" )
            print("q. Quit")

            command = input("User Input: ")
            if "1" in command:
                manned_voyages = self.get_manned_voyages()

                if manned_voyages:
                    print_dataclass_as_table(manned_voyages, Voyage)
                else:
                    print("No voyages found.")
                continue

            elif "2" in command:
                unmanned_voyages = self.get_unmanned_voyages()

                if unmanned_voyages:
                    print_dataclass_as_table(unmanned_voyages, Voyage)
                else:
                    print("No voyages found.")

                continue

            elif "q" in command:
                self.save_and_quit()

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
        print("q. Quit")
