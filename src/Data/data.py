import os
import csv


class EmployeeData:
    def __init__(self):
        print(os.getcwd())
        self.file_name = "src/Files/employees.csv"
    


    def get_all_employees(self):
        with open(self.file_name, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            employees_dict = [row for row in reader]
            return employees_dict


    def create_employee(self, employee):
        with open(self.file_name, "a", encoding="utf-8") as csv_file:
            fieldnames = ["name", "ssid", "job title", "license", "address", "phone_number", "e_mail_address", "home_phone"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            employee_data = list(map(lambda key: employee[key], employee.keys()))
            writer.writerow({"name": employee_data[0], "ssid": employee_data[1], "job title": employee_data[2], "license": employee_data[3], "address": employee_data[4], "phone_number": employee_data[5], "e_mail_address": employee_data[6], "home_phone": employee_data[7]})

    def update_employee(self, employee):
        pass 



class AirplaneData:
    def __init__(self):
        print(os.getcwd())
        self.file_name = "src/Files/airplanes.csv"