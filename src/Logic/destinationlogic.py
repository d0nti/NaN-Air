
class EmployeeLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_employee(self, employee):
        self.data_wrapper.create_employee(employee)

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()
    
    def search(self, filter):
        employees = self.data_wrapper.get_all_employees()  # Ná í alla starfsmenn
        filtered_employees = []  # Búa til lista til þess að henda uppl. inn um starfsmann, svo hægt sé að print-a hann
        for employee in employees:
            # Förum yfir hvert stak og gáum hvort eitthvað passi.
            if employee["name"] == filter or employee["ssid"] == filter or employee["job_title"] == filter:
                filtered_employees.append(employee)

        return filtered_employees

        
