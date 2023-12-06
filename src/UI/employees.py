from prettytable import Prettytable

INVALID_INPUT = "Invalid input! Please try again."
QUIT_MESSAGE = "Bye Bye!"



HEADER_EMPLOYEES = (
    "------------------------------"
    + "\n"
    + "  NaN Air - {}"
    + "\n"
    + "------------------------------"
)

"""HEADER_EMPLOYEES = (
      "------------------------------"
    + "\n"
    + "  NaN Air - Manage Employees"
    + "\n"
    + "------------------------------"
)

HEADER_INPUT_1 =(
      "------------------------------"
    + "\n"
    + "  NaN Air - Employee List"
    + "\n"
    + "------------------------------"
)

HEADER_INPUT_2 =(
      "------------------------------"
    + "\n"
    + "  NaN Air - Pilot List"
    + "\n"
    + "------------------------------"
)

HEADER_INPUT_3 =(
      "------------------------------"
    + "\n"
    + "  NaN Air - Flight Attendant List"
    + "\n"
    + "------------------------------"
)

HEADER_INPUT_4 =(
      "------------------------------"
    + "\n"
    + "  NaN Air - Heads of Service List"
    + "\n"
    + "------------------------------"
)

HEADER_INPUT_5 =(
      "------------------------------"
    + "\n"
    + "  NaN Air - Register New Employee"
    + "\n"
    + "------------------------------"
    + "Please Enter the Following Information:"
    + "\n"
    + "Employee Name, Employee SSID, Job Title, Pilot License (If applicable), Home Address, Phone Number, E-mail Address, Home Phone Number (optional)"
)"""


class Employees:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper


    def employees_menu_output(self):
        print(HEADER_EMPLOYEES.format("Manage Employees"))
        print("1. Employees")
        print("2. Register New Employee")
        print("3. Shift Plan")
        print("b. Back")
        print("q. Quit")


    def input_prompt_employees(self):
        while True:
            command = input("User Input: ")
            command = command.lower()

            if command == "q" or command == "q.":
                print(QUIT_MESSAGE)
                break
            elif command == "b" or command == "b.":
                break

            elif command == "1" or command == "1.":
                self.list_employees()

            elif command == "2" or command == "2.":
                pass  # eftir að implementa

            elif command == "3" or command == "3.":
                pass  # eftir að implementa

            else:
                print(INVALID_INPUT)


    def list_employees(self):
        print(HEADER_EMPLOYEES.format("Employee list"))
        employees = self.logic_wrapper.get_all_employees()

        if employees:
            table = PrettyTable()
            table.field_names = [
                "Name",
                "SSID",
                "Job Title",
                "License",
                "Address",
                "Phone Number",
                "E-mail Address",
            ]

            for employee in employees:
                table.add_row(
                    [
                        employee.get("name"),
                        employee.get("ssid"),
                        employee.get("job_title"),
                        employee.get("license"),
                        employee.get("address"),
                        employee.get("phone_number"),
                        employee.get("e-mail_address"),
                    ]
                )

            print(table)
        else:
            print("No employees found.")

        print("1. Search")
        print("2. Sort by:")
        command = input("User Input: ")

        if command == "2" or command == "2.":
            print("1. Captains")
            print("2. Co-Pilots")
            print("3. Flight Attendants")
            print("4. Heads of Service")

            self.get_sorted_list((input("User Input: ")))

        elif command == "1" or command == "1.":
            search_output = self.logic_wrapper.search(
                input("")
            )  # implementa search hér - sjá logic.py
            print(search_output)


    def get_sorted_list(self, command):
        self.command = command

        if command == "q" or command == "q.":
            pass
        
        elif command == "1" or command == "1.":
            # self.logic_wrapper.sort_by_captains()
            pass

        elif command == "2" or command == "2.":
            # self.logic_wrapper.sort_by_copilots()
            pass

        elif command == "3" or command == "3.":
            # self.logic_wrapper.sort_by_flight_attendants()
            pass

        elif command == "4" or command == "4.":
            # self.logic_wrapper.sort_by_heads_of_service()
            pass

        else:
            print(INVALID_INPUT)

        pass
