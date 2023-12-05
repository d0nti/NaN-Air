from Data.data import EmployeeData

class Logic_Data_Wrapper:
    def __init__(self):
        self.employee_data = EmployeeData()

    def get_all_employees(self):
        return self.employee_data.get_all_employees()

    def register_employee(self, employee):
        return self.employee_data.create_employee(employee)
    