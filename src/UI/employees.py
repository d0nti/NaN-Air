from prettytable import PrettyTable
from UI.Utils.Constants import UIConstants


class Employees:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper


    def employees_menu_output(self):
        print(UIConstants.HEADER.format(UIConstants.MANAGE_EMPLOYEES))
        print(UIConstants.MENU_OPTION.format(UIConstants.DISPLAY_EMPLOYEES, UIConstants.REGISTER_NEW_EMPLOYEE, UIConstants.SHIFT_PLAN, UIConstants.BACK, UIConstants.QUIT))
        
        # print("1. Employees")
        # print("2. Register New Employee")
        # print("3. Shift Plan")
        # print("b. Back")
        # print("q. Quit")
        # WHAT IS THIS^^?? IF NOT USEFUL, DELETE

    def input_prompt_employees(self):
        while True:
            command = input("User Input: ")
            command = command.lower()

            if command == "q" or command == "q.":
                print(UIConstants.QUIT_MESSAGE)
                break
            elif command == "b" or command == "b.":
                break

            elif command == "1" or command == "1.":
                self.list_employees()

            elif command == "2" or command == "2.":
                self.register_new_employee()

            elif command == "3" or command == "3.":
                pass  # eftir að implementa

            else:
                print(UIConstants.INVALID_INPUT)


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
            UIConstants.PHONE_NUMBER]
            
            # table.field_names = [
            #     "Name",
            #     "SSID",
            #     "Job Title",
            #     "Phone Number",
            #     "Address",
            # ]
            for employee in employees: # 
                table.add_row(
                    [
                        employee.ssid,
                        employee.name,
                        employee.job_title,
                        employee.rank,
                        employee.address,
                        employee.phone_nr,
                    ]
                )


            print(table)
        else:
            print(UIConstants.USER_NOT_FOUND)
            print(UIConstants.TABLE_OPTION_MENU.format(UIConstants.SEARCH, UIConstants.SORT_BY, UIConstants.BACK, UIConstants.QUIT))

        # print("1. Search")
        # print("2. Sort by:")
        # WHAT IS THIS^^?? IF NOT USEFUL, DELETE

        command = input("User Input: ")

        if command == "2" or command == "2.":
            print(UIConstants.SORT_BY_MENU.format(UIConstants.CAPTAINS, UIConstants.CO_PILOTS, UIConstants.FLIGHT_ATTENDTANTS, UIConstants.HEADS_OF_SERVICE, UIConstants.BACK, UIConstants.QUIT))
           
            # print("1. Captains")
            # print("2. Co-Pilots")
            # print("3. Flight Attendants")
            # print("4. Heads of Service"),
            # WHAT IS THIS^^?? IF NOT USEFUL, DELETE


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
            #print(*self.logic_wrapper.sort_by_captains())
            captains = self.logic_wrapper.sort_by_captains()
            
            if captains:
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

                for captain in captains:
                    table.add_row(
                        [
                            captain.ssid,
                            captain.name,
                            captain.job_title,
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
                            copilot.ssid,
                            copilot.name,
                            copilot.job_title,
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
                            flight_attendant.ssid,
                            flight_attendant.name,
                            flight_attendant.job_title,
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
                            head_of_service.ssid,
                            head_of_service.name,
                            head_of_service.job_title,
                            head_of_service.rank,
                            head_of_service.phone_nr,
                            head_of_service.address,
                        ]
                    )
            print(table)
            

        else:
            print(UIConstants.INVALID_INPUT)

        pass



    def register_new_employee(self):
        """ This function prints a new menu for the user, which allows 
            them to either create a new pilot or flight attendant.
            This will generate a list of all the information that the
            user wants to list for the new employee and sends it over
            to the employeelogic.py file for verification.
        """
        print(UIConstants.HEADER.format(UIConstants.REGISTER_NEW_EMPLOYEE))   
        print(UIConstants.TABLE_OPTION_MENU.format(UIConstants.REGISTER_NEW_PILOT, UIConstants.REGISTER_NEW_FLIGHT_ATTENDANT, UIConstants.BACK, UIConstants.QUIT))        
        
        
        # print("Choose an employee to register")
        # print("")
        # WHAT IS THIS^^?? IF NOT USEFUL, DELETE
        
        command = input("User input: ")
        if command == "1" or command == "1.":
            
            pilot_info = print(UIConstants.EMPLOYEE_INFORMATION_MESSAGE)
            pilot_info_print = list(UIConstants.EMPLOYEE_INFORMATION.split(", "))
            
            all_employee_information = []
            for i in pilot_info_print in range(len(pilot_info_print)-1):
                print(f"{i}", end = "")
                employye_information = input()
                all_employee_information.append(employye_information)


            self.logic_wrapper.register_pilot(pilot_info)
            
        elif command == "2" or command == "2.":
            
            flight_attendant_info = input("blablabla")
            self.logic_wrapper.register_flight_attendant(flight_attendant_info)

        elif command == "b" or command == "b.":
            pass

        elif command == "q" or command == "q.":
            pass

        else:
            print(UIConstants.INVALID_INPUT) # MAKE ERROR MSG PLS