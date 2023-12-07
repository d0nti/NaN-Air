class EmployeeLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_pilot(self, employee_info):
        self.data_wrapper.register_pilot(employee_info)

    def register_flight_attendant(self, employee_info):
        self.data_wrapper.register_flight_attendant(employee_info)

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()
    
    def sort_by_captains(self):
        return self.data_wrapper.sort_by_captains()
    
    def sort_by_co_pilots(self):
        return self.data_wrapper.sort_by_co_pilots()
    
    def sort_by_flight_attendants(self):
        return self.data_wrapper.sort_by_flight_attendants()
    
    def sort_by_heads_of_service(self):
        return self.data_wrapper.sort_by_heads_of_service()
    
    def search(self, filter):
        employees = self.data_wrapper.get_all_employees()  # Ná í alla starfsmenn
        filtered_employees = []  # Búa til lista til þess að henda uppl. inn um starfsmann, svo hægt sé að print-a hann
        for employee in employees:
            # Förum yfir hvert stak og gáum hvort eitthvað passi.
            if employee["name"] == filter or employee["ssid"] == filter or employee["job_title"] == filter:
                filtered_employees.append(employee)

        return filtered_employees







        


