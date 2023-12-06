from dataclasses import dataclass


@dataclass(order=True)
class Employee:
    name: str
    ssid: int
    job_title: str
    address: str
    phone_number: str
    e_mail_address: str
    #home_phone: str
    
    def __str__(self):
        return f"{self.name} {self.ssid} {self.job_title} {self.address} {self.phone_number} {self.e_mail_address}"

#nid,name,role,rank,licence,address,phone_nr,pref_nr,slot_param

@dataclass(order=True)
class Pilot(Employee):
    license: str


@dataclass(order=True)
class FlightAttendant(Employee):
    pass


@dataclass(order=True)
class CoPilot(Pilot):
    pass


@dataclass(order=True)
class Captain(Pilot):
    pass


@dataclass(order=True)
class HeadOfService(FlightAttendant):
    pass