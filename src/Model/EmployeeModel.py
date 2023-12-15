class Employee:
    def __init__(self, nid: str = None, name: str = None, role: str = None, rank: str = None, address: str = None, phone_nr: int = None, email_address: str = "", home_phone_nr: int = ""):
        self.nid = nid
        self.name = name
        self.role = role
        self.rank = rank
        self.address = address
        self.phone_nr = phone_nr
        self.email_address = email_address
        self.home_phone_nr = home_phone_nr

    def ___str__(self):
        return f"{self.nid} {self.name} {self.role} {self.rank} {self.address} {self.phone_nr}"

class Pilot(Employee):
    def __init__(
        self,
        nid=None,
        name=None,
        role=None,
        rank=None,
        address=None,
        phone_nr=None,
        email_address="",
        home_phone_nr="",
        license=None,
    ):
        self.license = license
        super().__init__(nid, name, role, rank, address, phone_nr, email_address, home_phone_nr)

    def ___str__(self):
        return f"{self.nid} {self.name} {self.role} {self.rank} {self.address} {self.phone_nr} {self.license}"

class FlightAttendant(Employee):
    def __init__(
        self,
        nid=None,
        name=None,
        role=None,
        rank=None,
        address=None,
        phone_nr=None,
        email_address="",
        home_phone_nr=""
    ):
        super().__init__(nid, name, role, rank, address, phone_nr, email_address, home_phone_nr)
