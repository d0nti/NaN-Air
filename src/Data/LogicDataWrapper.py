from Data.employeeData import EmployeeData
from Data.destinationData import DestinationData
from Data.planeData import AirplaneData

class Logic_Data_Wrapper:
    def __init__(self):
        self.employee_data = EmployeeData()
        self.destination_data = DestinationData()
        self.airplane_data = AirplaneData()

    def get_all_employees(self):
        return self.employee_data.get_all_employees()

    def register_employee(self, employee):
        return self.employee_data.create_employee(employee)

    def get_all_destinations(self):
        return self.destination_data.get_all_destinations()