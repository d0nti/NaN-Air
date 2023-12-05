class Employee:
    def __init__(self, name = None, ssid = None, job_title = None, license = None, address = None, phone_number = None, e_mail_address = None, home_phone = None):
        self.name = name
        self.ssid = ssid
        self.job_title = job_title
        self.address = address
        self.phone_number = phone_number
        self.e_mail_address = e_mail_address
        self.home_phone = home_phone

    def __str__(self):
        return f"name: {self.name}, SSID: {self.ssid}, Rank: {self.job_title},
        License: {self.license}, Address: {self.address}, Phone Number: {self.phone_number},
        E-mail Address: {self.e_mail_address}, Home Phone: {self.home_phone}"


class Pilot(Employee):
    def __init__(self, name):
        self.license = license
        super().__init__(name)

newEmployee = Employee("Jón", "2402922469")
newEmployee1 = Employee("Jón1", "2402922469")

print(Employee.name)

employees = [newEmployee, newEmployee1]

return employees