from Logic.Verifications.verifyemployee import VerifyPilot, VerifyFlightAttendant
from Model.EmployeeModel import Pilot, FlightAttendant

class EmployeeLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_pilot(self, employee_info):
        temp = VerifyPilot(employee_info, self.get_all_employees())
        temp.validatepilot()
        if temp:
            self.data_wrapper.register_pilot(employee_info)

    def register_flight_attendant(self, employee_info):
        temp = VerifyFlightAttendant(employee_info, self.get_all_employees())
        temp.validateflightattendant()
        if temp:
            self.data_wrapper.register_flight_attendant(employee_info)

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()
    
    def sort_by_captains(self):
        return self.data_wrapper.sort_by_captains()
    
    def sort_by_co_pilots(self):
        return self.data_wrapper.sort_by_co_pilots()
    
    def search_by_day(self, filter):
        return self.data_wrapper.search_by_day(filter)
    
    def search_by_not_day(self, filter):
        return self.data_wrapper.search_by_not_day(filter)
    
    def sort_by_flight_attendants(self):
        return self.data_wrapper.sort_by_flight_attendants()
    
    def sort_by_heads_of_service(self):
        return self.data_wrapper.sort_by_heads_of_service()
    
    def search_employee(self, filter):
        return self.data_wrapper.search_employee(filter)
    
    def update_pilot(self, employee_info: Pilot, new_employee_info: list[str]):
        if new_employee_info[0] != "": # 0 == role
            employee_info.role = new_employee_info[0]

        if new_employee_info[1] != "": # 1 == rank
            employee_info.rank = new_employee_info[1]

        if new_employee_info[2] != "": # 2 == licnese
            employee_info.license = new_employee_info[2]

        if new_employee_info[3] != "": # 3 == address
            employee_info.address = new_employee_info[3]

        if new_employee_info[4] != "": # 4 == phone number
            employee_info.phone_nr = new_employee_info[4]

        if new_employee_info[5] != "": # 5 == home phone number
            employee_info.home_phone_nr = new_employee_info[5]

        return self.data_wrapper.update_pilot(employee_info)

    def update_flight_attendant(self, employee_info: FlightAttendant, new_employee_info: list[str]):
        if new_employee_info[0] != "": # 0 == role
            employee_info.role = new_employee_info[0]

        if new_employee_info[1] != "": # 1 == rank
            employee_info.rank = new_employee_info[1]

        if new_employee_info[2] != "": # 2 == address
            employee_info.address = new_employee_info[2]

        if new_employee_info[3] != "": # 3 == phone number
            employee_info.phone_nr = new_employee_info[3]

        if new_employee_info[4] != "": # 4 == home phone number
            employee_info.home_phone_nr = new_employee_info[4]
        
        return self.data_wrapper.update_flight_attendant(employee_info)
    
    def get_shift_plan(self):
        return self.data_wrapper.get_shift_plan()
        



