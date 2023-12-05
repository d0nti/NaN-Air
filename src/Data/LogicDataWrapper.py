from Data.data import EmployeeData


class Logic_Data_Wrapper:
    def __init__(self):
        self.employee_data = EmployeeData()

    def get_all_customers(self):
        return self.employee_data.read_all_employees()

    def create_customer(self, employee):
        return self.employee_data.create_employee(employee) 