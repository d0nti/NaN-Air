from Logic.employeelogic import EmployeeLogic
from Logic.destinationlogic import DestinationLogic
from Logic.airplanelogic import AirplaneLogic
from Logic.voyageslogic import VoyagesLogic
from Data.DataWrapper import Logic_Data_Wrapper
from datetime import datetime
from Model.DestinationModel import Destination


class UI_Logic_Wrapper:
    def __init__(self):
        logic_data_wrapper_instance = Logic_Data_Wrapper()
        self.employee_logic = EmployeeLogic(logic_data_wrapper_instance)
        self.destination_logic = DestinationLogic(logic_data_wrapper_instance)
        self.voyages_logic = VoyagesLogic(logic_data_wrapper_instance)
        self.airplane_logic = AirplaneLogic(logic_data_wrapper_instance)

    #
    #       EMPLOYEE CALLS
    #

    def register_pilot(self, employee_info):
        return self.employee_logic.register_pilot(employee_info)

    def register_flight_attendant(self, emplpoyee_info):
        return self.employee_logic.register_flight_attendant(emplpoyee_info)

    def get_all_employees(self):
        return self.employee_logic.get_all_employees()

    def search_employee(self, filter):
        return self.employee_logic.search_employee(filter)

    def search_by_day(self, filter):
        return self.employee_logic.search_by_day(filter)

    def search_by_not_day(self, filter):
        return self.employee_logic.search_by_not_day(filter)

    def sort_by_captains(self):
        return self.employee_logic.sort_by_captains()

    def sort_by_co_pilots(self):
        return self.employee_logic.sort_by_co_pilots()

    def sort_by_flight_attendants(self):
        return self.employee_logic.sort_by_flight_attendants()

    def sort_by_heads_of_service(self):
        return self.employee_logic.sort_by_heads_of_service()

    def update_pilot(self, employee_info, new_employee_info):
        return self.employee_logic.update_pilot(employee_info, new_employee_info)

    def update_flight_attendant(self, employee_info, new_employee_info):
        return self.employee_logic.update_flight_attendant(
            employee_info, new_employee_info
        )

    def get_shift_plan(self):
        return self.employee_logic.get_shift_plan()

    #
    #       AIRPLANE CALLS
    #

    def get_all_airplanes(self):
        return self.airplane_logic.get_all_airplanes()

    def register_airplane(self, airplane_info):
        return self.airplane_logic.register_airplane(airplane_info)

    def search_airplane(self, filter):
        return self.airplane_logic.search_airplane(filter)

    #
    #       DESTINATION CALLS
    #

    def get_all_destinations(self):
        return self.destination_logic.get_all_destinations()

    def register_destination(self, destination_info):
        return self.destination_logic.register_destination(destination_info)

    def search_destination(self, filter):
        return self.destination_logic.search_destination(filter)

    def update_destination(
        self, destination: Destination, contact_name, contact_phone_nr
    ):
        return self.destination_logic.update_destination(
            destination, contact_name, contact_phone_nr
        )

    #
    #       VOYAGE CALLS
    #

    def get_all_voyages(self):
        return self.voyages_logic.get_all_voyages()

    def set_staff(self, voyage_id: str, **kwarg):
        return self.voyages_logic.set_staff(voyage_id, **kwarg)

    def write_voyages_to_disk(self):
        return self.voyages_logic.write_voyages_to_disk()

    def register_new_voyage(self, voyage_info):
        return self.voyages_logic.register_new_voyage(voyage_info)

    def find_voyage(self, filter):
        return self.voyages_logic.find_voyage(filter)

    def copy_to_new_date(self, voyage_id: str, new_date: datetime):
        return self.voyages_logic.copy_to_new_date(voyage_id, new_date)

    def make_recurring_voyage(
        self, voyage_id, interval_in_days: int, end_date: datetime
    ):
        return self.voyages_logic.make_recurring_voyage(
            voyage_id, interval_in_days, end_date
        )

    def get_manned_voyages(self):
        return self.voyages_logic.get_manned_voyages()

    def get_unmanned_voyages(self):
        return self.voyages_logic.get_unmanned_voyages()

    def voyages_an_employee_is_working(self, filter_date, employee_name):
        return self.voyages_logic.voyages_an_employee_is_working(
            filter_date, employee_name
        )
