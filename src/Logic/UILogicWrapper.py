from Logic.logic import EmployeeLogic
from Data.LogicDataWrapper import Logic_Data_Wrapper

class UI_Logic_Wrapper:
    def __init__(self):
        logic_data_wrapper_instance = Logic_Data_Wrapper()
        self.employee_logic = EmployeeLogic(logic_data_wrapper_instance)

    def create_employee(self, employee):
        """Takes in a customer object and forwards it to the data layer"""
        return self.employee_logic.create_employee(employee)

    def get_all_employees(self):
        return self.employee_logic.get_all_employees()
