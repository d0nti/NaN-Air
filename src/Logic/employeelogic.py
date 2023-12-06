class EmployeeLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_employee(self, employee):
        self.data_wrapper.create_employee(employee)

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()
    
    def sort_by_captains(self):
        return self.data_wrapper.sort_by_captains()
    
    def search(self, filter):
        employees = self.data_wrapper.get_all_employees()  # Ná í alla starfsmenn
        filtered_employees = []  # Búa til lista til þess að henda uppl. inn um starfsmann, svo hægt sé að print-a hann
        for employee in employees:
            # Förum yfir hvert stak og gáum hvort eitthvað passi.
            if employee["name"] == filter or employee["ssid"] == filter or employee["job_title"] == filter:
                filtered_employees.append(employee)

        return filtered_employees
    
    
    def verify_ssid(self):
        if len(self) == 10:
            if self[0:10].isdigit():
                return f"Valid SSID {self}."
            else:
                return f"Invalid SSID {self}. Make sure the characters are digits"
        else:
            return f"Invalid SSID length {self}. Make sure the length is 10 characters" 


    def verify_job_title(self):
        if self == "Pilot" or self == "CoPilot" or self == "Captain" or self == "Flight Attendant" or self == "Head of Service":
            return f"Valid job title {self}."
        else:
            return f"Invalid job title {self}. Make sure the job title is one of the following: Pilot, CoPilot, Captain, Flight Attendant, Head of Service"
    
    
    
        
