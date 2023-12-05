
class EmployeeLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_employee(self, employee):
        self.data_wrapper.create_employee(employee)

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()