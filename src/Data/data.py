import os
import csv
#import pandas as pd


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

#þetta á að virka!!!!!!!!!!!!! þetta skal virka plis
#þarf bara að importa pandas og þá á þetta að virka vonandi
'''
         #update the 
    def update_employee(self, employee_num, update_job_title, update_license, update_address, update_phone_number, update_e_mail_address, update_home_phone):
         #reading the csv file
         df = pd.read_csv("employees.csv")

         #update the 
         df.loc[employee_num, 'job_title'] = update_job_title
         df.loc[employee_num, 'licence'] = update_license
         df.loc[employee_num, 'adress'] = update_address
         df.loc[employee_num, 'phone_number'] = update_phone_number
         df.loc[employee_num, 'e-mail_adress'] = update_e_mail_address
         df.loc[employee_num, 'home_phone'] = update_home_phone

         #writing into the file
         df.to_csv("employees.csv", index=False)
'''

class PlaneData:
    def __init__(self):
        self.file_name = "src/Files/airplanes.csv"

    def get_all_airplanes(self):
        with open(self.file_name, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            airplanes_dict = [row for row in reader]
            return airplanes_dict

    def create_airplane(self, plane):
        with open(self.file_name, "a", encoding="utf-8") as csv_file:
            fieldnames = ["name", "type", "supplier", "seats"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            employee_data = list(map(lambda key: plane[key], employee.keys()))
            writer.writerow({"name": employee_data[0], "type": employee_data[1], "supplier": employee_data[2], "seats": employee_data[3]})

