class Employee:
    def __init__(self, name = None, ssid = None, job_title = None,
                 address = None, phone_number = None,
                 e_mail_address = None, home_phone = None):
        self.name = name
        self.ssid = ssid
        self.job_title = job_title
        self.address = address
        self.phone_number = phone_number
        self.e_mail_address = e_mail_address
        self.home_phone = home_phone


    def __str__(self):
        return f"name: {self.name}, SSID: {self.ssid}, Rank: {self.job_title},
        Address: {self.address}, Phone Number: {self.phone_number},
        E-mail Address: {self.e_mail_address}, Home Phone: {self.home_phone}"


class Pilot(Employee):
    def __init__(self, name = None, ssid = None, job_title = None,
                 address = None, phone_number = None,
                 e_mail_address = None,home_phone = None, license = None):
        super().__init__(name, ssid, job_title, address, phone_number,
                         e_mail_address, home_phone)
        self.license = license

    def __str__(self):
        return super().__str__() + f"{self.license}"


class FlightAttendant(Employee):
    def __init__(self, name = None, ssid = None, job_title = None,
                 address = None, phone_number = None,
                 e_mail_address = None, home_phone = None):
        super().__init__(name, ssid, job_title, address, phone_number,
                         e_mail_address, home_phone)



"""
newEmployee = Employee("Jón", "2402922469")
newEmployee1 = Employee("Jón1", "2402922469")

print(Employee.name)

employees = [newEmployee, newEmployee1]

return employees"""