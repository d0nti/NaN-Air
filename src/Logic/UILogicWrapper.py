from Logic.employeelogic import EmployeeLogic
from Logic.destinationlogic import DestinationLogic
from Logic.airplanelogic import AirplaneLogic
from Data.LogicDataWrapper import Logic_Data_Wrapper
from Logic.voyageslogic import VoyagesLogic


class UI_Logic_Wrapper:
    def __init__(self):
        logic_data_wrapper_instance = Logic_Data_Wrapper()
        self.employee_logic = EmployeeLogic(logic_data_wrapper_instance)
        self.destinationlogic = DestinationLogic(logic_data_wrapper_instance)
        self.voyageslogic = VoyagesLogic(logic_data_wrapper_instance)
        self.airplanelogic = AirplaneLogic(logic_data_wrapper_instance)

    def register_pilot(self, employee_info):
        return self.employee_logic.register_pilot(employee_info)

    def register_flight_attendant(self, emplpoyee_info):
        return self.employee_logic.register_flight_attendant(emplpoyee_info)

    def get_all_employees(self):
        return self.employee_logic.get_all_employees()

    def get_all_airplanes(self):
        return self.airplanelogic.get_all_airplanes()

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

    def get_all_destinations(self):
        return self.destinationlogic.get_all_destinations()

    def get_all_voyages(self):
        return self.voyageslogic.get_all_voyages()

    def register_new_voyage(self, voyage_info):
        return self.voyageslogic.register_new_voyage(voyage_info)
    
    def search_voyages(self, filter):
        return self.voyageslogic.search_voyages(filter)
        
    def copy_existing_voyage(self, voyage_info):
        return self.voyageslogic.copy_existing_voyage(voyage_info)
