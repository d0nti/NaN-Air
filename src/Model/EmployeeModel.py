class Employee:
    def __init__(self, nid="", name="", role="", rank="", address="", phone_nr=""):
        self.ssid = nid
        self.name = name
        self.job_title = role
        self.rank = rank
        self.address = address
        self.phone_nr = phone_nr


    def ___str__(self):
        return f"{self.ssid} {self.name} {self.job_title} {self.rank} {self.address} {self.phone_nr}"


class Pilot(Employee):
    def __init__(self, nid="", name="", job_title="", rank="", address="", phone_nr="", license = "" ):
        self.license = license
        super().__init__(nid, name, job_title, rank, address, phone_nr)
    
    def ___str__(self):
        return f"{self.ssid} {self.name} {self.job_title} {self.rank} {self.address} {self.phone_nr} {self.license}"



class FlightAttendant(Employee):
    def __init__(self, nid="", name="", job_title="", rank="", address="", phone_nr=""):
        super().__init__(nid, name, job_title, rank, address, phone_nr)

