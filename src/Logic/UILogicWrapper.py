from Logic.logic import EmployeeLogic
from Data.LogicDataWrapper import LogicDataWrapper

class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = LogicDataWrapper()
        self.employee_logic = EmployeeLogic(self.data_wrapper)

    def create_employee(self, employee):
        """Takes in a customer object and forwards it to the data layer"""
        return self.employee_logic.create_employee(employee)

    def get_all_employees(self):
        return self.employee_logic.get_all_employees() 