from dataclasses import dataclass

# class Destinations:
#     def __init__(self, number = str, country = str, airport_name = str, flight_time = None, distance_from_iceland = None, contact_name = None, contact_phone_number = None):
#         self.number = number
#         self.country = country
#         self.airport_name = airport_name
#         self.flight_time = flight_time
#         self.distance_from_iceland = distance_from_iceland
#         self.contact_name = contact_name
#         self.contact_phone_number = contact_phone_number

@dataclass (order=True)
class Destinations:
    name: str
    number: int
    country: str
    airport_name: str
    flight_time: int
    distance_from_iceland: int
    contact_name: str
    contact_phone_number: str


    def __str__(self):
        return f"{self.name} {self.number} {self.country} {self.airport_name},
        {self.flight_time} {self.distance_from_iceland} {self.contact_name},
        {self.contact_phone_number}"



