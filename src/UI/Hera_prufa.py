BOOKING_SYSTEM = "Booking System"
MANAGE_EMPLOYEES = "Manage Employees"
MANAGE_AIRPLANES = "Manage Airplanes"
MANAGE_DESTINATIONS = "Manage Destinations"
MANAGE_VOYAGES = "Manage Voyages"
DASH_SYMBOL = "-"
LENGTH_SYMBOL = 30
QUIT = "quit"


HEADER = (
    f"{DASH_SYMBOL * LENGTH_SYMBOL}"
    + "\n"
    + "  NaN Air - {location}"
    + "\n"
    + f"{DASH_SYMBOL * LENGTH_SYMBOL}"
)

MAIN_MENU = (

    "1. {}"
    + "\n"
    + "2. {}"
    + "\n"
    + "3. {}"
    + "\n"
    + "4. {}"
    + "\n"
    + "q. {}"
)

class UIConstants:
    MAIN_MENU = "This is the Main {} menu!!!"


print(UIConstants.MAIN_MENU.format("AAAAAAAA"))

class Destination:
    def __init__(
        self,
        name=None,
        country=None,
        airport=None,
        flight_time=None,
        distance_from_iceland=None,
        contact_name=None,
        contact_phone_nr=None,
    ):
        # self.destination_number = destination_number
        self.name = name
        self.country = country
        self.airport_call_sign = airport
        self.flight_time = flight_time
        self.distance_from_iceland = distance_from_iceland
        self.contact_name = contact_name
        self.contact_phone_nr = contact_phone_nr

    def ___str__(self):
        return f"{self.name} {self.country} {self.airport_call_sign} {self.flight_time} {self.distance_from_iceland}  {self.contact_name} {self.contact_phone_nr}"

name, country, airport, fligh_time, distance_from_iceland, contact_name, contact_phone_nr = ["Nuuk","Greenland","Nuuk_Airport","1_hour","1200km","Ivaana","+299-558-7709"]
x = Destination(name, country, airport, fligh_time, distance_from_iceland, contact_name, contact_phone_nr)