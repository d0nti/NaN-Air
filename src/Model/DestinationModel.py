class Destination:
    def __init__(self, destination_number = None, country = None, airport_call_sign = None, flight_time = None, distance_from_iceland = None, contact_name = None, contact_phone_number = None):
        self.destination_number = destination_number
        self.country = country
        self.airport_call_sign = airport_call_sign
        self.flight_time = flight_time
        self.distance_from_iceland = distance_from_iceland
        self.contact_name = contact_name
        self.contact_phone_number = contact_phone_number


    def ___str__(self):
        return f"{self.destination_number} {self.country} {self.airport_call_sign} {self.flight_time} {self.distance_from_iceland}"
