from Data.data import EmployeeData
from Models import employees

class EmployeeLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_employee(self, employee):
        """Takes in an employee object and forwards it to the data layer"""

        self.data_wrapper.create_employee(employee)

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()