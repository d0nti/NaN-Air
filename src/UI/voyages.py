from UI.Utils.Constants import UIConstants
from prettytable import PrettyTable
from Model.VoyageModel import Voyage
from dataclasses import asdict
from datetime import datetime
from typing import Iterable
import sys


class Voyages:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def voyages_menu_output(self):
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

    def show_voyage_menu(self):
        self.voyages_menu_output()
        return input("User Input: ").lower()

    def control_voyage_menu(self):
        # self.employees_menu_output()
        while (command := self.show_voyage_menu()) not in ("b", "b."):
            if command == "q" or command == "q.":
                print(UIConstants.QUIT_MESSAGE)
                sys.exit()
            elif command == "1" or command == "1.":
                self.list_all_voyages()
            elif command == "2" or command == "2.":
                self.register_voyage()
            elif command == "3" or command == "3.":
                self.copy_existing_voyage()
            elif command == "4" or command == "4.":
                self.make_reacurring_voyage()
            elif command == "5" or command == "5.":
                if (voyage := self.get_voyage()) is None:
                    continue
                self.control_man_voyages_menu(voyage)
            elif command == "6" or command == "6.":
                self.check_voyage_status()
            elif command == "7" or command == "7.":
                self.check_voyage_employee_is_working()
            else:
                print(UIConstants.INVALID_INPUT)

    # sub menu sort_by_man voyages
    def man_voyages_output(self, voyage):
        print(UIConstants.HEADER.format(UIConstants.CHOOSE_STAFF))
        if not voyage.captain:
            print(f"1. {UIConstants.ADD_CAPTAIN}")
        if not voyage.copilot:
            print(f"2. {UIConstants.ADD_CO_PILOTS}")
        if not voyage.flight_service_manager:
            print(f"3. {UIConstants.ADD_HEADS_OF_SERVICE}")
        if not voyage.flight_attendant:
            print(f"4. {UIConstants.ADD_FLIGHT_ATTENDTANTS}")
        print(f"b. {UIConstants.BACK} \n q. {UIConstants.QUIT}")

    def show_man_voyages_menu(self, voyage):
        self.man_voyages_output(voyage)
        return input("User Input: ").lower()

    def control_man_voyages_menu(self, voyage):
        while (command := self.show_man_voyages_menu(voyage)) not in ("b", "b."):
            if command == "q" or command == "q.":
                print(UIConstants.QUIT_MESSAGE)
                sys.exit()

            elif command == "1" or command == "1.":
                captains = self.logic_wrapper.sort_by_captains()
                self.print_employees_table(captains)
                name = input("Input name of captain: ")
                self.logic_wrapper.set_staff(voyage.id, captain=name)
                print(f"Successfully set captain {name} to voyage {voyage.id}")

            elif command == "2" or command == "2.":
                copilots = self.logic_wrapper.sort_by_co_pilots()
                self.print_employees_table(copilots)
                name = input("Input name of copilot: ")
                self.logic_wrapper.set_staff(voyage.id, copilot=name)
                print(f"Successfully set copilot {name} to voyage {voyage.id}")

            elif command == "3" or command == "3.":
                managers = self.logic_wrapper.sort_by_heads_of_service()
                self.print_employees_table(managers)
                name = input("Input name of flight service manager: ")
                self.logic_wrapper.set_staff(voyage.id, flight_service_manager=name)
                print(
                    f"Successfully set flight service manager {name} to voyage {voyage.id}"
                )

            elif command == "4" or command == "4.":
                attendants = self.logic_wrapper.sort_by_flight_attendants()
                self.print_employees_table(attendants)
                name = input("Input name of flight attendants: ")
                self.logic_wrapper.set_staff(voyage.id, flight_attendant=name)
                print(f"Successfully set flight attendant {name} to voyage {voyage.id}")

            elif command.lower() == "s":
                self.save_changes()

            else:
                print(UIConstants.INVALID_INPUT)
                print("command was:", command)
                input(UIConstants.CONTINUE_MESSAGE)

    def get_voyage(self):
        # TODO: Get input.
        # TODO: Validate input.
        # TODO: Get Voyage from logic wrapper.
        # TODO: If not voyage/if voyage manned ...

        while True:
            voyage_id = input(UIConstants.ENTER_VOYAGE_ID)

            voyage = self.logic_wrapper.find_voyage(voyage_id)

            if voyage is None:
                return UIConstants.NO_VOYAGES

            return voyage

        # while not (voyage_id := input(UIConstants.ENTER_VOYAGE_ID)):
        #     print("Error")

        # voyage = self.logic_wrapper.get_single_voyage_given_uuidge(voyage_id)

        # if voyage is None:
        #     return print(UIConstants.NO_VOYAGES)

        # if self.check_if_voyage_manned(voyage):
        #     return print("Voyage is fully staffed.")

        # return voyage

    # submenu display_voyages

    def display_voyages_output(self):
        print(UIConstants.HEADER.format(UIConstants.DISPLAY_VOYAGES))
        print(
            UIConstants.TWO_MENU_OPTION.format(
                UIConstants.LIST_MANNED_VOYAGES,
                UIConstants.LIST_UNMANNED_VOYAGES,
                UIConstants.BACK,
                UIConstants.QUIT,
            )
        )

    def show_display_voyages_menu(self):
        self.display_voyages_output()
        return input("User Input: ").lower()

    def control_display_voyages_menu(self):
        while (command := self.show_display_voyages_menu()) not in ("b", "b."):
            if command == "q" or command == "q.":
                print(UIConstants.QUIT_MESSAGE)
                sys.exit()

            elif command == "1" or command == "1.":
                print(UIConstants.HEADER.format(UIConstants.LIST_MANNED_VOYAGES))
                self.print_manned_voyages()

            elif command == "2" or command == "2.":
                print(UIConstants.HEADER.format(UIConstants.LIST_UNMANNED_VOYAGES))
                self.print_unmanned_voyages()

            else:
                print(UIConstants.INVALID_INPUT)
                print("command was:", command)
                input(UIConstants.CONTINUE_MESSAGE)

    def print_manned_voyages(self):
        manned_voyages = self.get_manned_voyages()

        if manned_voyages:
            self.print_dataclass_as_table(manned_voyages)
        else:
            print(UIConstants.NO_VOYAGES)

    def print_unmanned_voyages(self):
        unmanned_voyages = self.get_unmanned_voyages()

        if unmanned_voyages:
            self.print_dataclass_as_table(unmanned_voyages)
        else:
            print(UIConstants.NO_VOYAGES)

    def print_employees_table(self, employees):
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

    def save_changes(self):
        self.logic_wrapper.write_voyages_to_disk()
        print(UIConstants.CHANGES_SAVED)

    def register_voyage(self):
        voyage_info_print = UIConstants.REGISTER_VOYAGE_INFO.split(", ")

        all_voyage_information = []
        for voyage_field in voyage_info_print:
            print(f"{voyage_field}: ", end=" ")
            voyage_information = input()
            all_voyage_information.append(voyage_information)

        # Converting list to dataclass by using '*' operator that converts list to fields in dataclass
        all_voyage_information[1] = datetime.fromisoformat(all_voyage_information[1])
        all_voyage_information[2] = datetime.fromisoformat(all_voyage_information[2])
        new_voyage = Voyage(*all_voyage_information)

        self.print_dataclass_as_table(new_voyage)

        self.logic_wrapper.register_new_voyage(new_voyage)
        print(UIConstants.NEW_VOYAGE_REGISTERED)
        print("Press s to save changes: ")
        command = input().lower()
        if command == "s":
            self.save_changes()

    def copy_existing_voyage(self):
        voyage_id = input(UIConstants.ENTER_VOYAGE_ID)
        new_date = input(UIConstants.ENTER_NEW_DATE)

        self.logic_wrapper.copy_to_new_date(voyage_id, datetime.fromisoformat(new_date))
        print(UIConstants.VOYAGE_COPIED)
        self.print_dataclass_as_table(self.logic_wrapper.get_all_voyages())

    def make_reacurring_voyage(self):
        voyage_id = input(UIConstants.ENTER_VOYAGE_ID)
        interval_in_days = int(input(UIConstants.INTERVAL_DAYS))
        end_date = input(UIConstants.ENTER_END_DATE)

        self.logic_wrapper.make_recurring_voyage(
            voyage_id, interval_in_days, datetime.fromisoformat(end_date)
        )
        print(UIConstants.VOYAGE_MADE_RECURRING)
        self.print_dataclass_as_table(self.logic_wrapper.get_all_voyages())

    def check_voyage_status(self):
        voyage_id = input(UIConstants.ENTER_VOYAGE_ID)
        voyage = self.logic_wrapper.find_voyage(voyage_id)

        self.print_dataclass_as_table(voyage)

    def check_voyage_employee_is_working(self):
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

    def list_all_voyages(self):
        """Lists all voyages from a file."""
        voyages = self.logic_wrapper.get_all_voyages()
        if voyages:
            self.print_dataclass_as_table(voyages)
        else:
            print(UIConstants.NO_VOYAGES)

    def populate_voyage(self):
        voyage_id = input(UIConstants.ENTER_VOYAGE_ID)
        while True:
            voyage = self.logic_wrapper.find_voyage(voyage_id)

            if not voyage:
                print(UIConstants.NO_VOYAGES)
                return

            if self.check_if_voyage_manned(voyage):
                print("Voyage is fully staffed.")
                return

            self.choose_staff_prompt(voyage)

    def print_dataclass_as_table_out(self, instances):
        """Prints a dataclass as a table."""

        if not isinstance(instances, Iterable):
            instances = [instances]
        elif not instances:
            return

        table = PrettyTable(
            field_names=[field for field in Voyage.__dataclass_fields__.keys()]
        )
        for instance in instances:
            table.add_row([v for _, v in asdict(instance).items()])

        print(table)
