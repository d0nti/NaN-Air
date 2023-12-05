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


print(HEADER.format(location = "Booking System"))

print(MAIN_MENU.format(MANAGE_VOYAGES, MANAGE_EMPLOYEES, MANAGE_DESTINATIONS, MANAGE_AIRPLANES, QUIT))




