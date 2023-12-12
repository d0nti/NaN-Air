from Data.employeeData import EmployeeData
from Data.destinationData import DestinationData
from Data.planeData import AirplaneData
from Data.voyagesdata import VoyageData
from datetime import datetime


class Logic_Data_Wrapper:
    def __init__(self):
        self.employee_data = EmployeeData()
        self.destination_data = DestinationData()
        self.airplane_data = AirplaneData()
        self.voyagedata = VoyageData(VoyageData.read_voyages_from_disk())

    def write_voyages_to_disk(self):
        VoyageData.write_voyages_to_disk(self.voyagedata.get_all_voyages())

    def register_pilot(self, employee_info):
        return self.employee_data.register_pilot(employee_info)

    def register_flight_attendant(self, employee_info):
        return self.employee_data.register_flight_attendant(employee_info)

    def set_staff(self, voyage_id: str, **kwarg):
        return self.voyagedata.set_staff(voyage_id, **kwarg)

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

    def register_airplane(self, airplane_info):
        return self.airplane_data.register_airplane(airplane_info)

    #
    #       VOYAGES DATA FUNCTIONS
    #

    def get_all_voyages(self):
        return self.voyagedata.get_all_voyages()

    def register_new_voyage(self, voyage):
        return self.voyagedata.register_new_voyage(voyage)

    def find_voyage(self, id):
        return self.voyagedata.find_voyage_by_id(id)

    def copy_to_new_date(self, voyage_id: str, new_date: datetime):
        return self.voyagedata.copy_to_new_date(voyage_id, new_date)

    def make_recurring_voyage(
        self, voyage_id, interval_in_days: int, end_date: datetime
    ):
        return self.voyagedata.make_recurring_voyage(
            voyage_id, interval_in_days, end_date
        )

    def get_manned_voyages(self):
        return self.voyagedata.get_manned_voyages()

    def get_unmanned_voyages(self):
        return self.voyagedata.get_unmanned_voyages()

    def update_pilot(self, employee_info):
        return self.employee_data.update_pilot(employee_info)

    def update_flight_attendant(self, employee_info):
        return self.employee_data.update_flight_attendant(employee_info)
