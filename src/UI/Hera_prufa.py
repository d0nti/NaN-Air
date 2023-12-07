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

