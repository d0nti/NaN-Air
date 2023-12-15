class Destination:
    def __init__(
        self,
        name: str=None,
        country: str=None,
        airport: str=None,
        flight_time: int=None,
        distance_from_Iceland: int=None,
        contact_name: str=None,
        contact_phone_nr: int=None,
    ):
        # self.destination_number = destination_number
        self.name = name
        self.country = country
        self.airport = airport.strip("_Airport")
        self.flight_time = flight_time.strip("_hour")
        self.distance_from_Iceland = distance_from_Iceland.strip("km")
        self.contact_name = contact_name
        self.contact_phone_nr = contact_phone_nr

    def ___str__(self):
        return f"{self.name} {self.country} {self.airport} {self.flight_time} {self.distance_from_Iceland}  {self.contact_name} {self.contact_phone_nr}"
