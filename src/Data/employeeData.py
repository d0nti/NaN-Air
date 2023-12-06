from Model.EmployeeModel import Employee
import csv

class EmployeeData:
    def __init__(self):
        self.file_name = "src/Files/employees.csv"
        self.employee = []
        self.Employee = Employee()
        

    def get_all_employees(self):
        with open(self.file_name, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                line = line.split(",")
                for y in line:
                    self.employee += self.Employee(y)
                      

    def create_employee(self, employee_dict):
        with open(self.file_name, "w+") as employee_file:
            employee_file.write("name,ssid,job_title,address,phone_number,e-mail_address,home_phone,license")

            for employee in employee_dict.values():
                name = employee.get_name()
                ssid = employee.get_ssid()
                job_title = employee.get_job_title()
                adress = employee.get_adress()
                phone_number = employee.get_phone_number()
                email = employee.get_email()
                home_phone = employee.get_home_phone()
                license = employee.get_license()

                employee_file.write("\n{},{},{},{},{},{},{},{}".format(name, ssid, job_title, adress, phone_number, email, home_phone, license,))







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

