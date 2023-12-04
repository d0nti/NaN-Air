import os
import csv

class EmployeeData:
    def __init__(self):
        print(os.getcwd())
        self.file_name = "Models/employees.csv"


    def get_all_employees(self):
        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimeter=",")
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    pass



