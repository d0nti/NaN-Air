
class Destinations:
    def __init__(self, number = None, country = None, airport_name = None, flight_time = None, distance_from_iceland = None, contact_name = None, contact_phone_number = None):
        self.number = number
        self.country = country
        self.airport_name = airport_name
        self.flight_time = flight_time
        self.distance_from_iceland = distance_from_iceland
        self.contact_name = contact_name
        self.contact_phone_number = contact_phone_number


    def __str__(self):
        return f": {self.name}, SSID: {self.ssid}, Rank: {self.job_title},
        License: {self.license}, Address: {self.address}, Phone Number: {self.phone_number},
        E-mail Address: {self.e_mail_address}, Home Phone: {self.home_phone}"