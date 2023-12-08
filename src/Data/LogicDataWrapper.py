from Data.employeeData import EmployeeData
from Data.destinationData import DestinationData
from Data.planeData import AirplaneData
from Data.voyagesdata import VoyageData


class Logic_Data_Wrapper:
    def __init__(self):
        self.employee_data = EmployeeData()
        self.destination_data = DestinationData()
        self.airplane_data = AirplaneData()
        self.voyagedata = VoyageData()

    def register_pilot(self, employee_info):
        return self.employee_data.register_pilot(employee_info)

    def register_flight_attendant(self, employee_info):
        return self.employee_data.register_flight_attendant(employee_info)

    def get_all_employees(self):
        return self.employee_data.get_all_employees()

    def get_all_destinations(self):
        return self.destination_data.get_all_destinations()

    def sort_by_captains(self):
        return self.employee_data.sort_by_captains()

    def sort_by_co_pilots(self):
        return self.employee_data.sort_by_co_pilots()

    def sort_by_flight_attendants(self):
        return self.employee_data.sort_by_flight_attendants()

    def sort_by_heads_of_service(self):
        return self.employee_data.sort_by_heads_of_service()

    def search(self, filter):
        return self.employee_data.search(filter)

#
#       AIRPLANE FUNCTION CALLS FROM HERE DOWN
#

    def get_all_airplanes(self):
        return self.airplane_data.get_all_airplanes()


#       VOYAGES DATA FUNCTIONS
    def get_all_voyages(self):
        return self.voyagedata.get_all_voyages()
    
    def register_new_voyage(self, voyage_info):
        return self.voyagedata.register_new_voyage(voyage_info)
