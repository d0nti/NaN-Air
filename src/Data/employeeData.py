from Model.EmployeeModel import Employee
from Model.EmployeeModel import Pilot
from Model.EmployeeModel import FlightAttendant

import csv



class EmployeeData:
    def __init__(self):
        self.file_name = "src/Files/crew.csv"
        self.number_of_employees = 0

#frá fyrirlestri
    def get_all_employees(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile: 
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.number_of_employees += 1
                if row["licence"] != "N/A":
                    ret_list.append(Pilot(row["nid"], row["name"], row["role"],
                                         row["rank"], row["address"],
                                         row["licence"], row["phone_nr"]))
                elif row["licence"] == "N/A":
                    ret_list.append(FlightAttendant(row(["nid"], row["name"], row["role"],
                                                    row["rank"], row["address"],
                                                    row["phone_nr"])))

                return ret_list

    def sort_by_captains(self):
        extra_sort = self.get_all_employees()
        pilot_list = []

        for employee in extra_sort:
            if employee.get('rank') == "Pilot":
                pilot_list.append(employee)

        return pilot_list

             


    def create_employee(self, employee):
        with open(self.file_name, "a") as csvfile:
            fieldnames = ["nid", "name", "role", "rank", "license", "address", "phone_nr"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"nid": employee.nid, "name": employee.name,
                             "role": employee.role, "rank": employee.rank,
                             "license": employee.licence, "address": employee.address,
                             "phone_nr": employee.phone_nr})




    # def get_all_employees(self):
    #     with open(self.file_name, "r") as csv_file:
    #         reader = csv.DictReader(csv_file)
    #         employees_dict = [row for row in reader]
    #         return employees_dict


    # def create_employee(self, employee):
    #     with open(self.file_name, "a", encoding="utf-8") as csv_file:
    #         fieldnames = ["name", "ssid", "job title", "license", "address", "phone_number", "e_mail_address", "home_phone"]
    #         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #         employee_data = list(map(lambda key: employee[key], employee.keys()))
    #         writer.writerow({"name": employee_data[0], "ssid": employee_data[1], "job title": employee_data[2], "license": employee_data[3], "address": employee_data[4], "phone_number": employee_data[5], "e_mail_address": employee_data[6], "home_phone": employee_data[7]})

