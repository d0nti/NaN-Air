from Logic.Verifications.verifyemployee import VerifyPilot, VerifyFlightAttendant

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
    
    def sort_by_flight_attendants(self):
        return self.data_wrapper.sort_by_flight_attendants()
    
    def sort_by_heads_of_service(self):
        return self.data_wrapper.sort_by_heads_of_service()
    
    def search_employee(self, filter):
        return self.data_wrapper.search_employee(filter)
    
    def update_pilot(self, employee_info):
        return self.data_wrapper.update_pilot(employee_info)

    def update_flight_attendant(self, employee_info):
        return self.data_wrapper.update_flight_attendant(employee_info)
    
    def get_shift_plan(self):
        return self.data_wrapper.get_shift_plan()
        



