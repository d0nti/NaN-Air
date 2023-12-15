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
    DESTINATION_INFO = "Name, Country, Airport, Flight Time, Distance from Iceland, Contact Name, Contact Phone Number"
    REGISTER_DESTINATION_MESSAGE = "A new destination has been added to the system"
    COUNTRY = "Country"
    AIRPORT = "Airport"
    FLIGHT_DURATION = "Flight Duration"
    DISTANCE_FROM_ICELAND = "Distance from Iceland"
    CONTACT_NAME = "Contact Name"
    CONTACT_PHONE_NUMBER = "Contact Phone Number"
    NO_DESTINATIONS_REGISTERED = "No destinations registered"
    SUCCESSFULL_REGISTRATION_FOR_DESTINATION = (
        "Congrats a new destination has been registered"
    )
    UPDATE_DESTINATION = "Update Destination"
    UPDATE_DESTINATION_MESSAGE = (
        "Please enter in the name of the destination you would like to update"
    )
    UPDATE_DESTINATION_INFO = "Contact Name, Contact Phone Number"
    SUCCESSFULL_UPDATE_FOR_DESTINATION = "Information has been sucessfully updated"

    EMPLOYEE_SEARCH_PARAM = "Enter search filter (SSID, Name, license or Job Title): "
    DISPLAY_EMPLOYEES = "Display Employess"
    REGISTER_NEW_EMPLOYEE = "Register New Employee"
    REGISTER_NEW_FLIGHT_ATTENDANT = "Register New Flight Attendant"
    REGISTER_NEW_PILOT = "Register New Pilot"
    UPDATE_EMPLOYEE = "Update Employee"
    UPDATE_PILOT = "Update Pilot"
    UPDATE_FLIGHT_ATTENDANT = "Update Flight Attendant"
    SHIFT_PLAN = "Shift Plan"
    FILTER_EMPLOYEES = "Filter employees"
    EMPLOYEE_LIST = "Employee list"
    EMPLOYEE_INFORMATION = "Employee Name, Employee SSID, Job Title, Pilot License (If applicable), Home Address, Phone Number, E-mail Address, Home Phone Number (optional), License"
    REGISTER_EMPLOYEE_INFO = (
        "SSID, Name, Rank, Address, Phonenumber, Home Phone Number(optional), License"
    )
    UPDATE_EMPLOYEE_INFO_MESSAGE = (
        "If you don't wish to change a given detail, leave it empty. \n"
    )
    WRONG_SSID_INPUTTED_MESSAGE = "You have entered the wrong ssid, please try again "
    UPDATE_PILOT_INPUT = "Role, Rank, License, Address, Phone number, Home Phone Number"
    UPDATE_FLIGHT_ATTENDANT_INPUT = (
        "Role, Rank, Address, Phone number, Home Phone Number"
    )
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
    REGISTER_VOYAGE_INFO = "UUID, Destination, Departure Time (HH:MM), Departure Date (YYYY-MM-DD), Arrival Time (HH:MM), Arrival Date (YYYY-MM-DD), Captain (Name), Co-Pilot (Name), Flight Service Manager (Name), Flight Attendant (Name)"
    SHIFT_START_DATE = "Shift Start Date (YYYY-MM-DD)"
    SHIFT_START_TIME = "Shift Start Time (HH-MM)"
    SHIFT_END_DATE = "Shift End Date (YYYY-MM-DD)"
    SHIFT_END_TIME = "Shift End Time (HH-MM)"
    DISPLAY_SHIFT_PLAN = "Display Shift Plan"
    WORKING_ON_A_SPECIFIC_DAY = "Working on a specific day"
    NOT_WORKING_ON_A_SPECIFIC_DAY = "Not working on a specific day"
    EMPLOYEES_WORKING_MESSAGE = "These employees here above are working on"
    EMPLOYEES_NOT_WORKING = "These employees here above are not working on"

    REGISTER_NEW_VOYAGE = "Register New Voyage"
    EDIT_VOYAGE = "Edit Voyage"
    POPULATE_VOYAGE = "Populate Voyage"
    DISPLAY_VOYAGES = "Display Voyages"
    CHECK_VOYAGE_STATUS = "Check Voyage Status"
    DISPLAY_VOYAGES = "Display Voyages"
    REGISTER_NEW_VOYAGES = "Register New Voyage"
    COPY_EXISTING_VOYAGE = "Copy Existing Voyage"
    MAKE_RECURRING_VOYAGE = "Make Recurring Voyage"
    CHOOSE_STAFF = "Choose Staff"
    CHECK_VOYAGE_STATUS = "Check Voyage Status"
    CHECK_VOYAGES_AN_EMP_IS_WORKING = "Check Voyages an Employee is Working"
    LIST_MANNED_VOYAGES = "List Manned Voyages"
    LIST_UNMANNED_VOYAGES = "List Unmanned Voyages"

    INVALID_INPUT = "Invalid input! Please try again."
    QUIT_MESSAGE = "Bye Bye!"
    DASH_SYMBOL = "-"
    LENGTH_SYMBOL = 43
    QUIT = "Quit"
    BACK = "Back"
    SEARCH = "Search by:"
    SORT_BY = "Sort by:"
    SORT_BY_MENU_OUTPUT = (
        "1. Captains"
        + "\n"
        + "2. Co-Pilots"
        + "\n"
        + "3. Flight Attendants"
        + "\n"
        + "4. Heads of Service"
        + "\n"
    )
    USER_NOT_FOUND = "User Not Found!"
    CONTINUE_MESSAGE = "Press enter to continue"
    GO_BACK_INSTRUCTION = "Press Q and enter to go back"
    INFORMATION_MESSAGE = (
        "Please Enter the Following Information in the following order:"
    )
    SEARCH_DESTINATION_MESSAGE = " Please enter in one of the following information for the destination/s you would like to search:"
    SEARCH_DESTINATION_MESSAGE_CONTINUE = "Name, Country, Airport, Flight duration, Distance from Iceland, Contact Name, Contact phone number"
    DESTINATION_SEARCH_FILTER_NOT_FOUND_ERROR_MESSAGE = (
        "Note: No destination matched the inputted information "
    )
    NOTHING_IN_SEARCH = "Nothing in search"
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

    ONE_MENU_OPTION = "1. {}" + "\n" + "b. {}" + "\n" + "q. {}"

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

    FIVE_MENU_OPTION = (
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

    SEVEN_MENU_OPTION = (
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
        + "6. {}"
        + "\n"
        + "7. {}"
        + "\n"
        + "b. {}"
        + "\n"
        + "q. {}"
    )

    # Destination Error Messages

    DESTINATION_NAME_ERROR_MESSAGE = "Note: All characters must be in the alphabet"
    DESTINATION_NAME_EXISTS_ERROR_MESSAGE = (
        "Note: The name name for the destination already exists"
    )

    DESTINATION_COUNTRY_ERROR_MESSAGE = "Note: All character must be in the alphabet"
    DESTINATION_AIRPORT_ERROR_MESSAGE = "Note: All character must be in the alphabet"
    DESTINATION_AIRPORT_EXISTS_ERROR_MESSAGE = (
        "Note: The name for the airport already exists"
    )

    DESTINATION_DISTANCE_ERROR_MESSAGE = "Note: All characters must be digit"
    DESTINATION_FLIGHT_TIME_ERROR_MESSAGE = "Note: All character mus be digit"
    DESTINATION_CONTACT_ERROR_MESSAGE = "Note: All characters must be in the alphabet"
    DESTINATION_CONTACT_NUMBER_ERROR_MESSAGE = (
        "Note: the phone number must include + and a 10 digit number"
    )

    DESTINATION_CONTACT_NUMBER_EXISTS_ERROR_MESSAGE = (
        "Note: The phone number already exists"
    )

    # Employee Error Messages

    EMPLOYEE_SSID_LENGTH_ERROR = (
        "Note: The SSID you entered is either too short or too long"
    )
    EMPLOYEE_SSID_EXISTS_ERROR = (
        "Note: The SSID you entered is already assigned to an employee"
    )
    EMPLOYEE_SSID_FORMAT_ERROR = (
        "Note: The SSID you entered contains non-numerical characters"
    )
    EMPLOYEE_PILOT_AGE_ERROR = (
        "Note: The pilot you tried to register is either too old or too young"
    )
    EMPLOYEE_NAME_LONG_ERROR = "Note: The name you tried to enter is too long"
    EMPLOYEE_NAME_SHORT_ERROR = "Note: The name you tried to enter is too short"
    EMPLOYEE_ROLE_ERROR = "Note: The role you tried to assign does not exist"
    EMPLOYEE_RANK_ERROR = "Note: The rank you tried to assign does not exist"
    EMPLOYEE_ADDRESS_FORMAT_ERROR = (
        "Note: The address you tried to enter is of an invalid format"
    )
    EMPLOYEE_PHONE_NUMBER_ERROR = "Note: The phone number you tried to assign to that employee is of an invalid format"
    EMPLOYEE_HOME_PHONE_NUMBER_ERROR = "Note: The home phone number you tried to assign to that employee is of an invalid format"
    PILOT_LICENSE_ERROR = "Note: The license you tried to enter is invalid"
    SUCCESSFULL_REGISTRATION_FOR_PILOT = (
        "Congratulations! You've successfully registered a pilot."
    )
    SUCCESSFULL_REGISTRATION_FOR_FLIGHT_ATTENDANT = (
        "Congratulations! You've successfully registered a flight attendant."
    )
