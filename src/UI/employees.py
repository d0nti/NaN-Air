from prettytable import PrettyTable
from UI.Utils.Constants import UIConstants
from Model.EmployeeModel import Pilot, FlightAttendant
from Logic.Verifications.verifyemployee import(
EmployeeSsidLenError,EmployeeSsidExistsError,SsidNumError,
EmployeeAgeError,EmployeeNameLongError,EmployeeNameShortError,
EmployeeRoleError,EmployeeRankError,EmployeeAddressError,
EmployeePhoneNumberError,EmployeeHomePhoneNumberError,PilotLicenseError)
import sys


class Employees:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def employees_menu_output(self):  #
        print(UIConstants.HEADER.format(UIConstants.MANAGE_EMPLOYEES))
        print(
            UIConstants.FOUR_MENU_OPTION.format(
                UIConstants.DISPLAY_EMPLOYEES,
                UIConstants.REGISTER_NEW_EMPLOYEE,
                UIConstants.UPDATE_EMPLOYEE,
                UIConstants.SHIFT_PLAN,
                UIConstants.BACK,
                UIConstants.QUIT,
            )
        )

        # print("1. Display Employees")
        # print("2. Register New Employee")
        # print("3. Update Employee")
        # print("4. Shift Plan")
        # print("b. Back")
        # print("q. Quit")
    
    def dostuff(self):
        self.employees_menu_output()
        return input("User Input: ").lower()

    def input_prompt_employees(self):
        # self.employees_menu_output()
        while (command := self.dostuff()) not in ("b", "b."):
            if command == "q" or command == "q.":
                sys.exit()
            elif command == "1" or command == "1.":
                # self.list_employees()
                self.list_employees()
            elif command == "2" or command == "2.":
                self.register_new_employee()
            elif command == "3" or command == "3.":
                self.update_employee()
            elif command == "4" or command == "4.":
                self.display_shift_plan()
            else:
                print(UIConstants.INVALID_INPUT)
                print("command was:", command)
                input("press enter to continue")
        #end while
    # end func 
    def list_employees(self):
        print(UIConstants.HEADER.format(UIConstants.DISPLAY_EMPLOYEES))
        employees = self.logic_wrapper.get_all_employees()

        if employees:
            table = PrettyTable()
            table.field_names = [
                UIConstants.SSID,
                UIConstants.NAME,
                UIConstants.JOB_TITLE,
                UIConstants.RANK,
                UIConstants.ADDRESS,
                UIConstants.PHONE_NUMBER,
            ]

            # table.field_names = [
            #     "Name",
            #     "SSID",
            #     "Job Title",
            #     "Phone Number",
            #     "Address",
            # ]
            for employee in employees:  # fix e
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

            # nid,name,role,rank,licence,address,phone_nr,

            print(table)
            print(
                UIConstants.TWO_MENU_OPTION.format(
                    UIConstants.SEARCH,
                    UIConstants.SORT_BY,
                    UIConstants.BACK,
                    UIConstants.QUIT,
                )
            )

        else:
            print(UIConstants.USER_NOT_FOUND)


        # print("1. Search")
        # print("2. Sort by:")

        command = input("User Input: ")

        if command == "b" or command == "b.":
            print("Hér er ég")
            self.employees_menu_output()
            back = self.input_prompt_employees() ## Prufa back = næst
            if back == "b":
                pass

        elif command == "2" or command == "2.":
            print(
                UIConstants.FOUR_MENU_OPTION.format(
                    UIConstants.CAPTAINS,
                    UIConstants.CO_PILOTS,
                    UIConstants.FLIGHT_ATTENDTANTS,
                    UIConstants.HEADS_OF_SERVICE,
                    UIConstants.BACK,
                    UIConstants.QUIT,
                )
            )

            # print("1. Captains")
            # print("2. Co-Pilots")
            # print("3. Flight Attendants")
            # print("4. Heads of Service"),

            self.get_sorted_list((input("User Input: ")))
        # nid,name,role,rank,license,address,phone_nr,pref_nr,slot_param
        elif command == "1" or command == "1.":
            filter = input("Enter search filter (SSID, Name, license or Job Title): ")
            filtered_employees = self.logic_wrapper.search_employee(filter)
            table = PrettyTable()

            table.field_names = [
                UIConstants.SSID,
                UIConstants.NAME,
                UIConstants.JOB_TITLE,
                UIConstants.RANK,
                UIConstants.LICENSE,
                UIConstants.ADDRESS,
                UIConstants.PHONE_NUMBER,
            ]

            for employee in filtered_employees:
                print(employee)
                table.add_row(
                    [
                        employee.nid,
                        employee.name,
                        employee.role,
                        employee.rank,
                        employee.license,
                        employee.address,
                        employee.phone_nr,
                    ]
                )

            print(table)
            print(
                UIConstants.TWO_MENU_OPTION.format(
                    UIConstants.SEARCH,
                    UIConstants.SORT_BY,
                    UIConstants.BACK,
                    UIConstants.QUIT,
                )
            )

        else:
            pass

    def get_sorted_list(self, command):
        self.command = command

        if command == "q" or command == "q.":
            print(UIConstants.QUIT_MESSAGE)
            sys.exit()

        elif command == "b" or command == "b.":
            print("Hér er ég")
            self.employees_menu_output()
            self.input_prompt_employees
            return "b"

        elif command == "1" or command == "1.":
            # print(*self.logic_wrapper.sort_by_captains())
            captains = self.logic_wrapper.sort_by_captains()

            if captains:
                table = PrettyTable()

                # nid,name,role,rank,license,address,phone_nr,pref_nr,slot_param
                table.field_names = [
                    UIConstants.SSID,
                    UIConstants.NAME,
                    UIConstants.JOB_TITLE,
                    UIConstants.RANK,
                    UIConstants.LICENSE,
                    UIConstants.PHONE_NUMBER,
                    UIConstants.ADDRESS,
                ]

                for captain in captains:
                    table.add_row(
                        [
                            captain.nid,
                            captain.name,
                            captain.role,
                            captain.rank,
                            captain.license,
                            captain.phone_nr,
                            captain.address,
                        ]
                    )
            print(table)

        elif command == "2" or command == "2.":
            copilots = self.logic_wrapper.sort_by_co_pilots()

            if copilots:
                table = PrettyTable()

                table.field_names = [
                    UIConstants.SSID,
                    UIConstants.NAME,
                    UIConstants.JOB_TITLE,
                    UIConstants.RANK,
                    UIConstants.LICENSE,
                    UIConstants.PHONE_NUMBER,
                    UIConstants.ADDRESS,
                ]

                for copilot in copilots:
                    table.add_row(
                        [
                            copilot.nid,
                            copilot.name,
                            copilot.role,
                            copilot.rank,
                            copilot.license,
                            copilot.phone_nr,
                            copilot.address,
                        ]
                    )
            print(table)

        elif command == "3" or command == "3.":
            flight_attendants = self.logic_wrapper.sort_by_flight_attendants()

            if flight_attendants:
                table = PrettyTable()

                table.field_names = [
                    UIConstants.SSID,
                    UIConstants.NAME,
                    UIConstants.JOB_TITLE,
                    UIConstants.RANK,
                    UIConstants.PHONE_NUMBER,
                    UIConstants.ADDRESS,
                ]

                for flight_attendant in flight_attendants:
                    table.add_row(
                        [
                            flight_attendant.nid,
                            flight_attendant.name,
                            flight_attendant.role,
                            flight_attendant.rank,
                            flight_attendant.phone_nr,
                            flight_attendant.address,
                        ]
                    )
            print(table)

        elif command == "4" or command == "4.":
            heads_of_services = self.logic_wrapper.sort_by_heads_of_service()

            if heads_of_services:
                table = PrettyTable()

                table.field_names = [
                    UIConstants.SSID,
                    UIConstants.NAME,
                    UIConstants.JOB_TITLE,
                    UIConstants.RANK,
                    UIConstants.PHONE_NUMBER,
                    UIConstants.ADDRESS,
                ]

                for head_of_service in heads_of_services:
                    table.add_row(
                        [
                            head_of_service.nid,
                            head_of_service.name,
                            head_of_service.role,
                            head_of_service.rank,
                            head_of_service.phone_nr,
                            head_of_service.address,
                        ]
                    )
            print(table)

            print()

        else:
            print(UIConstants.INVALID_INPUT)

        pass


    def register_new_employee(self):
        """This function prints a new menu for the user, which allows
        them to either create a new pilot or flight attendant.
        This will generate a list of all the information that the
        user wants to list for the new employee and sends it over
        to the employeelogic.py file for verification.
        """
        print(UIConstants.HEADER.format(UIConstants.REGISTER_NEW_EMPLOYEE))
        print(
            UIConstants.TWO_MENU_OPTION.format(
                UIConstants.REGISTER_NEW_PILOT,
                UIConstants.REGISTER_NEW_FLIGHT_ATTENDANT,
                UIConstants.BACK,
                UIConstants.QUIT,
            )
        )

        
        command = input("User input: ")
        
        if command == "1" or command == "1.":
            self.register_new_pilot()

        elif command == "2" or command == "2.":
            self.register_new_flight_attendant()

        elif command == "b" or command == "b.":
            print("REG GO BACK!")
            self.employees_menu_output()
            self.input_prompt_employees() #Þetta virkar
            return "b"

        elif command == "q" or command == "q.":
            pass

        else:
            print(UIConstants.INVALID_INPUT)  # MAKE ERROR MSG PLS

    def update_employee(self):
        print(UIConstants.HEADER.format(UIConstants.UPDATE_EMPLOYEE))
        print(
            UIConstants.TWO_MENU_OPTION.format(
                UIConstants.UPDATE_PILOT,
                UIConstants.UPDATE_FLIGHT_ATTENDANT,
                UIConstants.BACK,
                UIConstants.QUIT,
            )
        )

        command = input("User input: ")
        if command == "1" or command == "1.":
            print(UIConstants.HEADER.format(UIConstants.UPDATE_PILOT))
            print("If you don't wish to change a given detail, leave it empty. \n")
            while True:
                ssid = input("Enter the SSID of the pilot to update: ")
                if len(ssid) == 10: # Hér er hægt að skrifa hvaða ssid sem er og fá error ef það er ekki til
                    if self.logic_wrapper.search_employee(ssid)[0]:                     # IDK    THIS
                        pilot_to_change = self.logic_wrapper.search_employee(ssid)[0]   #     IF      WORKS
                    if pilot_to_change:
                        break
                    else:
                        print("You have entered the wrong ssid, please try again. ")
                        pass

            print(UIConstants.UPDATE_PILOT_INPUT)
            pilot_info_print = UIConstants.UPDATE_PILOT_INPUT.split(", ")

            all_pilot_information = []
            for i in pilot_info_print:
                print(f"{i}", end=" ")
                new_information = input()
                all_pilot_information.append(new_information)

            self.logic_wrapper.update_pilot(pilot_to_change, all_pilot_information)

        elif command == "2" or command == "2.":
            self.update_flight_attendant()

        elif command == "b" or command == "b.": #####################<=======
            print("GO BACK!")
            self.employees_menu_output()
            self.input_prompt_employees() #Þetta virkar
            return "b"

        elif command == "q" or command == "q.":
            pass

        else:
            print(UIConstants.INVALID_INPUT)  # ERROR :)


    def display_shift_plan(self):
        # get the shift plan from employeeData.py
        ret_list = self.logic_wrapper.get_shift_plan()


        table = PrettyTable()

        table.field_names = [
            "SSID",
            "Name",
            "Shift Start Date",
            "Shift Start Time",
            "Shift End Date",
            "Shift End Time",
        ]

        # add data rows to the table
        for row in ret_list:
            table.add_row(row)

        # Print the table
        print(UIConstants.HEADER.format(UIConstants.SHIFT_PLAN))
        print(table)

        # Menu for searching by working or not working on a specific day
        # print("Search by:")
        print("1. Working on a specific day")
        print("2. Not working on a specific day")
<<<<<<< HEAD
        print("b. Back")
        print("q. Quit")
=======
        print("b. back")
        print("q. quit")
>>>>>>> e8a0abb9376eaf41d71872d4672add752757463e

        command = input("Enter your choice: ")

        if command == "q" or command == "q.":
            print(UIConstants.QUIT_MESSAGE)
            sys.exit()

        elif command == "b" or command == "b.":
                return "b"

        elif command == "1" or command == "1.":
            filter = input("Enter the day to search for: ") #get the day to search for
            results = self.logic_wrapper.search_by_day(filter)

            table = PrettyTable()

            table.field_names = [
                UIConstants.SSID,
                UIConstants.NAME,
                UIConstants.SHIFT_START_DATE,
                UIConstants.SHIFT_START_TIME,
                UIConstants.SHIFT_END_DATE,
                UIConstants.SHIFT_END_TIME,
            ]

            for row in results:
                table.add_row([
                    row['nid'],
                    row['name'],
                    row['shift_start_date'],
                    row['shift_start_time'],
                    row['shift_end_date'],
                    row['shift_end_time']
                ])

            # Print the table
            print(table)
            print(f"These employees here above are working on {filter}")

        elif command == "2" or command == "2.":
            filter = input("Enter the day to search for: ") #get the day to search for
            results = self.logic_wrapper.search_by_not_day(filter)

            table = PrettyTable()

            table.field_names = [
                "NID",
                "Name",
                "Shift Start Date",
                "Shift Start Time",
                "Shift End Date",
                "Shift End Time",
            ]

            # Add data rows to the table
            for row in results:
                table.add_row([
                    row['nid'],
                    row['name'],
                    row['shift_start_date'],
                    row['shift_start_time'],
                    row['shift_end_date'],
                    row['shift_end_time']
                ])
        
            # Print the table
            print(table)
            print(f"These employees here above are not working on {filter}")

<<<<<<< HEAD
        elif command == "b" or command == "b.": #####################<=======
            print("GO BACK!")
            self.employees_menu_output()
            self.input_prompt_employees() #Þetta virkar
            return "b"
=======

    def register_new_pilot(self):
        print(UIConstants.HEADER.format(UIConstants.REGISTER_NEW_PILOT))
        print(UIConstants.INFORMATION_MESSAGE)
        pilot_info_print = UIConstants.REGISTER_EMPLOYEE_INFO.split(", ")

        all_pilot_information = []

        is_new_pilot_valid = False
        while not is_new_pilot_valid:
            try:
                for option in pilot_info_print:
                    print(f"{option}", end=" ")
                    pilot_information = input()
                    all_pilot_information.append(pilot_information)

                if len(all_pilot_information) == 6:
                    ssid, name, rank, address, phone_nr, license = [
                        all_pilot_information[i]
                        for i in range(0, (len(all_pilot_information)))
                    ]
                    self.logic_wrapper.register_pilot(
                        Pilot(ssid, name, "Pilot", rank, address, phone_nr, license)
                    )

                elif len(all_pilot_information) == 7:
                    ssid, name, rank, address, phone_nr, home_phone_nr, license = [
                        all_pilot_information[i]
                        for i in range(0, (len(all_pilot_information)))
                    ]
                    self.logic_wrapper.register_pilot(
                        Pilot(
                            ssid, name, "Pilot", rank, address, phone_nr, home_phone_nr, license
                        )
                    )

            except EmployeeSsidLenError:
                print(UIConstants.EMPLOYEE_SSID_LENGTH_ERROR)

            except EmployeeSsidExistsError:
                print(UIConstants.EMPLOYEE_SSID_EXISTS_ERROR)

            except SsidNumError:
                print(UIConstants.EMPLOYEE_SSID_FORMAT_ERROR)
            
            except EmployeeAgeError:
                print(UIConstants.EMPLOYEE_PILOT_AGE_ERROR)
            
            except EmployeeNameLongError:
                print(UIConstants.EMPLOYEE_NAME_LONG_ERROR)
            
            except EmployeeNameShortError:
                print(UIConstants.EMPLOYEE_NAME_SHORT_ERROR)
            
            except EmployeeRoleError:
                print(UIConstants.EMPLOYEE_ROLE_ERROR)
            
            except EmployeeRankError: 
                print(UIConstants.EMPLOYEE_RANK_ERROR)
            
            except EmployeeAddressError:
                print(UIConstants.EMPLOYEE_ADDRESS_FORMAT_ERROR)
            
            except EmployeePhoneNumberError:
                print(UIConstants.EMPLOYEE_PHONE_NUMBER_ERROR)
            
            except EmployeeHomePhoneNumberError:
                print(UIConstants.EMPLOYEE_HOME_PHONE_NUMBER_ERROR)
            
            except PilotLicenseError:
                print(UIConstants.PILOT_LICENSE_ERROR)

            else:
                print(UIConstants.SUCCESSFULL_REGISTRATION_FOR_PILOT)
                is_new_pilot_valid = True

    def register_new_flight_attendant(self):
        print(UIConstants.HEADER.format(UIConstants.REGISTER_NEW_FLIGHT_ATTENDANT))
        print(UIConstants.INFORMATION_MESSAGE)
        flight_attendant_info_print = UIConstants.REGISTER_EMPLOYEE_INFO.split(", ")
        flight_attendant_info_print = flight_attendant_info_print[0:-2]

        all_flight_attendant_information = []
        
        is_new_flight_attendant_valid = False
        while not is_new_flight_attendant_valid:
            try:
                for i in flight_attendant_info_print[0 : len(flight_attendant_info_print)]:
                    print(f"{i}", end=" ")
                    flight_attendant_information = input()
                    all_flight_attendant_information.append(flight_attendant_information)

                if len(all_flight_attendant_information) == 5:
                    ssid, name, rank, address, phone_nr = [
                        all_flight_attendant_information[i]
                        for i in range(0, (len(all_flight_attendant_information)))
                    ]
                    self.logic_wrapper.register_flight_attendant(
                        FlightAttendant(ssid, name, "Cabincrew", rank, address, phone_nr)
                    )

                elif len(all_flight_attendant_information) == 6:
                    ssid, name, rank, address, phone_nr, home_phone_nr = [
                        all_flight_attendant_information[i]
                        for i in range(0, (len(all_flight_attendant_information)))
                    ]
                    self.logic_wrapper.register_flight_attendant(
                        FlightAttendant(
                            ssid, name, "Cabincrew", rank, address, phone_nr, home_phone_nr
                        )
                    )

            except EmployeeSsidLenError:
                print(UIConstants.EMPLOYEE_SSID_LENGTH_ERROR)

            except EmployeeSsidExistsError:
                print(UIConstants.EMPLOYEE_SSID_EXISTS_ERROR)

            except SsidNumError:
                print(UIConstants.EMPLOYEE_SSID_FORMAT_ERROR)
            
            except EmployeeAgeError:
                print(UIConstants.EMPLOYEE_PILOT_AGE_ERROR)
            
            except EmployeeNameLongError:
                print(UIConstants.EMPLOYEE_NAME_LONG_ERROR)
            
            except EmployeeNameShortError:
                print(UIConstants.EMPLOYEE_NAME_SHORT_ERROR)
            
            except EmployeeRoleError:
                print(UIConstants.EMPLOYEE_ROLE_ERROR)
            
            except EmployeeRankError: 
                print(UIConstants.EMPLOYEE_RANK_ERROR)
            
            except EmployeeAddressError:
                print(UIConstants.EMPLOYEE_ADDRESS_FORMAT_ERROR)
            
            except EmployeePhoneNumberError:
                print(UIConstants.EMPLOYEE_PHONE_NUMBER_ERROR)
            
            except EmployeeHomePhoneNumberError:
                print(UIConstants.EMPLOYEE_HOME_PHONE_NUMBER_ERROR)
            
            except PilotLicenseError:
                print(UIConstants.PILOT_LICENSE_ERROR)

            else:
                print(UIConstants.SUCCESSFULL_REGISTRATION_FOR_PILOT)
                is_new_flight_attendant_valid = True


    def update_flight_attendant(self):
        print(UIConstants.HEADER.format(UIConstants.UPDATE_FLIGHT_ATTENDANT))
        print("If you don't wish to change a given detail, leave it empty. \n")
        while True:
            ssid = input("Enter the SSID of the flight attendant to update: ")
            if len(ssid) == 10:
                flight_attendant_to_change = self.logic_wrapper.search_employee(ssid)[0]
                if flight_attendant_to_change:
                    break
            else:
                print("You have entered the wrong SSID, please try again. ")
                pass

        print(UIConstants.UPDATE_FLIGHT_ATTENDANT_INPUT)
        flight_attendant_info_print = UIConstants.UPDATE_FLIGHT_ATTENDANT_INPUT.split(", ")
        all_flight_attendant_information = []

        for i in flight_attendant_info_print:
            print(f"{i}", end=" ")
            new_information = input()
            all_flight_attendant_information.append(new_information)
        
        self.logic_wrapper.update_flight_attendant(flight_attendant_to_change, all_flight_attendant_information)
>>>>>>> e8a0abb9376eaf41d71872d4672add752757463e
