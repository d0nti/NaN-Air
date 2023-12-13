class UIConstants:
    BOOKING_SYSTEM = "Booking System"
    MANAGE_EMPLOYEES = "Manage Employees"
    MANAGE_AIRPLANES = "Manage Airplanes"
    MANAGE_DESTINATIONS = "Manage Destinations"
    MANAGE_VOYAGES = "Manage Voyages"

    DISPLAY_AIRPLANES = "Display Airplanes"
    REGISTER_NEW_AIRPLANE = "Register New Airplane"
    FIND_AIRPLANE = "Find Airplane"
    PRINT_AIRPLANE_EFFICIENCY = "Print Airplane Efficiency"
    TYPE = "Type"
    SEATS = "Seats"
    SUPPLIER = "Supplier"

    DISPLAY_DESTINATIONS = "Display Destinations"
    REGISTER_NEW_DESTINATION = "Register New Destination"
    FIND_DESTINATION = "Find Destination"
    DESTINATION_IINFO = "Name, Country, Airport, Flight Time, Distance from Iceland, Contact Name, Contact Phone Number"
    REGISTER_DESTINATION_MESSAGE = "A new destination has been added to the system"
    COUNTRY = "Country"
    AIRPORT = "Airport"
    FLIGHT_DURATION = "Flight Duration"
    DISTANCE_FROM_ICELAND = "Distance from Iceland"
    CONTACT_NAME = "Contact Name"
    CONTACT_PHONE_NUMBER = "Contact Phone Number"
    NO_DESTINATIONS_REGISTERED = "No destinations registered"
    SUCCESFULL_REGISTRATION_FOR_DESTINATION = (
        "Congrats a new destination has been registered"
    )
    UPDATE_DESTINATION = "Update Destination"
    UPDATE_DESTINATION_MESSAGE = (
        "Please enter in the name of the destination you would like to update"
    )
    UPDATE_DESTINATION_INFO = "Contact Name, Contact Phone Number"

    DISPLAY_EMPLOYEES = "Display Employess"
    REGISTER_NEW_EMPLOYEE = "Register New Employee"
    REGISTER_NEW_FLIGHT_ATTENDANT = "Register New Flight Attendant"
    REGISTER_NEW_PILOT = "Register New Pilot"
    UPDATE_EMPLOYEE = "Update Employee"
    UPDATE_PILOT = "Update Pilot"
    UPDATE_FLIGHT_ATTENDANT = "Update Flight Attendant"
    SHIFT_PLAN = "Shift Plan"
    EMPLOYEE_LIST = "Employee list"
    EMPLOYEE_INFORMATION = "Employee Name, Employee SSID, Job Title, Pilot License (If applicable), Home Address, Phone Number, E-mail Address, Home Phone Number (optional), License"
    REGISTER_EMPLOYEE_INFO = (
        "SSID, Name, Rank, Address, Phonenumber, Home Phone Number(optional), License"
    )
    UPDATE_EMPLOYEE_INPUT = "Role, Rank, License, Address, Phone number"
    NAME = "Name"
    SSID = "SSID"
    JOB_TITLE = "Job Title"
    LICENSE = "License"
    RANK = "Rank"
    ADDRESS = "Address"
    PHONE_NUMBER = "Phone Number"
    HOME_PHONE_NUMBER = "Home Phone Number (optional)"
    E_MAIL_ADDRESS = "E-mail Address"
    NO_EMPLOYEE_FOUND = "No employee found"
    CAPTAINS = "Captains"
    CO_PILOTS = "Co-Pilots"
    FLIGHT_ATTENDTANTS = "Flight Attendants"
    HEADS_OF_SERVICE = "Heads of Service"
    REGISTER_VOYAGE_INFO = "UUID, Destination, Departure Time (HH:MM), Departure Date (YYYY-MM-DD), Arrival Time (HH:MM), Arrival Date (YYYY-MM-DD), Captain (National ID), Co-Pilot (National ID), Flight Service Manager (National ID), Flight Attendant (National ID)"
    SHIFT_START_DATE = "Shift Start Date (YYYY-MM-DD)"
    SHIFT_START_TIME = "Shift Start Time (HH-MM)"
    SHIFT_END_DATE = "Shift End Date (YYYY-MM-DD)"
    SHIFT_END_TIME = "Shift End Time (HH-MM)"
    DISPLAY_SHIFT_PLAN = "Display Shift Plan"

    REGISTER_NEW_VOYAGE = "Register New Voyage"
    EDIT_VOYAGE = "Edit Voyage"
    POPULATE_VOYAGE = "Populate Voyage"
    DISPLAY_VOYAGES = "Display Voyages"
    CHECK_VOYAGE_STATUS = "Check Voyage Status"

    INVALID_INPUT = "Invalid input! Please try again."
    QUIT_MESSAGE = "Bye Bye!"
    DASH_SYMBOL = "-"
    LENGTH_SYMBOL = 43
    QUIT = "Quit"
    BACK = "Back"
    SEARCH = "Search"
    SORT_BY = "Sort by:"
    USER_NOT_FOUND = "User Not Found!"
    CONTINUE_MESSAGE = "Press enter to continue"
    GO_BACK_INSTRUCTION = "Press Q and enter to go back"
    INFORMATION_MESSAGE = (
        "Please Enter the Following Information in the following order:"
    )

    HEADER = (
        f"{DASH_SYMBOL * LENGTH_SYMBOL}"
        + "\n"
        + "  NaN Air - {}"
        + "\n"
        + f"{DASH_SYMBOL * LENGTH_SYMBOL}"
    )

    MAIN_MENU = (
        "1. {}" + "\n" + "2. {}" + "\n" + "3. {}" + "\n" + "4. {}" + "\n" + "q. {}"
    )

    THREE_MENU_OPTION = (
        "1. {}" + "\n" + "2. {}" + "\n" + "3. {}" + "\n" + "b. {}" + "\n" + "q. {}"
    )

    TWO_MENU_OPTION = "1. {}" + "\n" + "2. {}" + "\n" + "b. {}" + "\n" + "q. {}"

    FOUR_MENU_OPTION = (
        "1. {}"
        + "\n"
        + "2. {}"
        + "\n"
        + "3. {}"
        + "\n"
        + "4. {}"
        + "\n"
        + "b. {}"
        + "\n"
        + "q. {}"
    )

    FIVE_THREE_MENU_OPTION = (
        "1. {}"
        + "\n"
        + "2. {}"
        + "\n"
        + "3. {}"
        + "\n"
        + "4. {}"
        + "\n"
        + "5. {}"
        + "\n"
        + "b. {}"
        + "\n"
        + "q. {}"
    )
