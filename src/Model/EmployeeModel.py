class Employee:
    def __init__(self, nid= None, name= None, role= None, rank= None, address= None, phone_nr= None, home_phone_nr = None):
        self.ssid = nid
        self.name = name
        self.job_title = role
        self.rank = rank
        self.address = address
        self.phone_nr = phone_nr
        self.home_phone_nr = home_phone_nr # NOT YET IMPLEMENTED IN DATA


    def ___str__(self):
        return f"{self.ssid} {self.name} {self.job_title} {self.rank} {self.address} {self.phone_nr}"


class Pilot(Employee):
    def __init__(self, nid= None, name= None, job_title= None, rank= None, address= None, phone_nr= None, home_phone_nr = None, license =  None ):
        self.license = license
        super().__init__(nid, name, job_title, rank, address, phone_nr, home_phone_nr)
    
    def ___str__(self):
        return f"{self.ssid} {self.name} {self.job_title} {self.rank} {self.address} {self.phone_nr} {self.license}"



class FlightAttendant(Employee):
    def __init__(self, nid= None, name= None, job_title= None, rank= None, address= None, phone_nr= None, home_phone_nr = None):
        super().__init__(nid, name, job_title, rank, address, phone_nr, home_phone_nr)

