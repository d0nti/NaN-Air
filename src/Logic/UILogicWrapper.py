from Logic.employeelogic import EmployeeLogic
from Data.LogicDataWrapper import Logic_Data_Wrapper

class UI_Logic_Wrapper:
    def __init__(self):
        self.logic_data_wrapper_instance = Logic_Data_Wrapper()
        self.employee_logic = EmployeeLogic(self.logic_data_wrapper_instance)

    def register_pilot(self, employee_info):
        return self.employee_logic.register_pilot(employee_info)
    
    def register_flight_attendant(self, emplpoyee_info):
        return self.employee_logic.register_flight_attendant(emplpoyee_info)

    def get_all_employees(self):
        return self.employee_logic.get_all_employees()

    def search(self, filter):
        return self.employee_logic.search(filter)
    
    def sort_by_captains(self):
        return self.employee_logic.sort_by_captains()
    
    def sort_by_co_pilots(self):
        return self.employee_logic.sort_by_co_pilots()

    def sort_by_flight_attendants(self):
        return self.employee_logic.sort_by_flight_attendants()
    
    def sort_by_heads_of_service(self):
        return self.employee_logic.sort_by_heads_of_service()
    

#
#       AIRPLANE FUNCTION CALLS FROM HERE DOWN
#
    def get_all_airplanes(self):
        return self.airplane_data.get_all_airplanes()

    