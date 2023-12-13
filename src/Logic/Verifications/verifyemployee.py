class EmployeeSsidLenError(Exception):
    pass
class EmployeeSsidExistsError(Exception):
    pass
class SsidNumError(Exception):
    pass
class EmployeeAgeError(Exception):
    pass
class EmployeeNameLongError(Exception):
    pass
class EmployeeNameShortError(Exception):
    pass
class EmployeeRankError(Exception):
    pass
class EmployeeAddressError(Exception):
    pass
class EmployeePhoneNumberError(Exception):
    pass
class EmployeeHomePhoneNumberError(Exception):
    pass
class PilotLicenseError(Exception):
    pass

MAX_EMP_NAME_LEN = 100
MIN_EMP_NAME_LEN = 8

MAX_PILOT_BIRTH_YEAR = "1958"
MAX_PILOT_BIRTH_YEAR = list(MAX_PILOT_BIRTH_YEAR)
MIN_PILOT_BIRTH_YEAR = "1998"
MIN_PILOT_BIRTH_YEAR = list(MIN_PILOT_BIRTH_YEAR)



class VerifyFlightAttendant:
    def __init__(self, employee_info: object, data: list):
        """ verification class with methods to verify every input from user when
            creating a new flight attendant employee.
            Meant to take in an employee class object.
        """
        self.data = data
        self.nid = employee_info.nid
        self.name = employee_info.name
        self.role = employee_info.role
        self.rank = employee_info.rank
        self.address = employee_info.address
        self.phone_nr = employee_info.phone_nr
        self.home_phone = employee_info.home_phone_nr


    def verify_flight_attendant_helper(self, info_type):
        """ info_type must be a string with the values 'nid', 'name', 'role',
            'rank', 'address', 'phone_nr', 'home_phone_nr' or 'license'.
            This func will then return a list of all registered strings 
        """

        in_use_info = []

        for i in range(len(self.data)):
            temp = self.data[i]
            in_use_info.append(getattr(temp, info_type))

        return in_use_info


    def Ssid(self):
        """ Checks if ssid is of length 10, checks if ssid is only numbers,
            checks if pilot is older than 65 years or younger than 25,
        """

        temp1 = list(self.nid)
        temp1 = temp1[4:6]
        temp1 = str(temp1[0]) + str(temp1[-1])

        if len(self.nid) != 10:
            raise SsidNumError
        elif not self.nid.isdigit():
            raise SsidNumError
        if self.nid in self.verify_flight_attendant_helper("nid"):     # Checks if nid already exists
            raise EmployeeSsidExistsError 
        else:
            return True


    def Name(self):
        """ Checks if a pilot's name is longer than MAX_EMP_NAME_LEN
            or shorter than MIN_EMP_NAME_LEN
        """

        if len(self.name) > MAX_EMP_NAME_LEN:
            raise EmployeeNameLongError
        elif len(self.name) < MIN_EMP_NAME_LEN:
            raise EmployeeNameShortError
        else:
            return True


    def Rank(self):
        """ Verifies that a pilot's rank is either pilot or copilot
        """
        
        if self.rank.lower() != "flight attendant" and self.rank.lower() != "flight service manager":
            raise EmployeeRankError
        else:
            return True


    def Address(self):
        """ Splits the address string into a list and verifies that the first 
            item is not digits and that the last item is digits
        """

        temp = self.address.split(" ")
        
        if temp[0].isdigit():
            raise EmployeeAddressError
        elif not temp[-1].isdigit():
            raise EmployeeAddressError
        else:
            return True


    def PhoneNumber(self):
        """ Checks that a phone number is 11 digits long
            and that all but the first item are digits
        """
        
        if len(str(self.phone_nr)) != 7:
            raise EmployeePhoneNumberError
        if not str(self.phone_nr).isdigit():
            raise EmployeePhoneNumberError


    def HomePhoneNumber(self):
        """ Checks that a home phone number is 11 digits long
            and that all but the first item are digits
        """

        if len(str(self.home_phone)) != 7:
            raise EmployeeHomePhoneNumberError
        if not str(self.phone_nr).isdigit():
            raise EmployeeHomePhoneNumberError


    def validateflightattendant(self):
        self.Ssid()
        self.Name()
        self.Rank()
        self.Address()
        self.PhoneNumber()
        if self.home_phone != "":
            self.HomePhoneNumber()
    



class VerifyPilot(VerifyFlightAttendant):
    def __init__(self, employee_info: object, data: list):
        """ verification class with methods to verify every input from user when
            creating a new pilot employee.
            Meant to take in an employee class object.
        """
        
        self.data = data
        self.nid = employee_info.nid
        self.name = employee_info.name
        self.role = employee_info.role
        self.rank = employee_info.rank
        self.address = employee_info.address
        self.phone_nr = employee_info.phone_nr
        self.home_phone = employee_info.home_phone_nr
        self.license = employee_info.license


    def verify_pilot_helper(self, info_type: str):
        """ info_type must be a string with the values 'nid', 'name', 'role',
            'rank', 'address', 'phone_nr', 'home_phone_nr' or 'license'.
            This func will then return a list of all registered strings 
        """

        in_use_info = []

        for i in range(len(self.data)):
            temp = self.data[i]
            in_use_info.append(getattr(temp, info_type))

        return in_use_info


    def Ssid(self):
        """ Checks if ssid is of length 10, checks if ssid is only numbers,
            checks if pilot is older than 65 years or younger than 25,
        """

        temp1 = list(self.nid)                  # Transform nid to a list data type for later indexing
        temp1 = temp1[4:6]                      # Takes the "age" numericals from ssid and assigns them to temp1 
        temp1 = str(temp1[0]) + str(temp1[-1])  # Splices both numericals from the line above into a string and assigns them to temp1

        temp2 = MAX_PILOT_BIRTH_YEAR[1:3]       # Takes the numerical values needed from MAX_PILOT_BIRTH_YEAR and assigns them to temp2
        temp2 = str(temp2[0]) + str(temp2[-1])  # Splices both numericals from the line above into a string and assigns them to temp2

        temp3 = MIN_PILOT_BIRTH_YEAR[1:3]       # Takes the numerical values needed from MIN_PILOT_BIRTH_YEAR and assigns them to temp3
        temp3 = str(temp3[0]) + str(temp3[-1])  # Splices both numericals from the line above into a string and assigns them to temp3


        if len(self.nid) != 10:     # If ssid number is not 10 digits
            raise SsidNumError
        if not self.nid.isdigit():    # Else if all numbers in the ssid are not digits
            raise SsidNumError
        if int(temp1) < int(temp2) and int(temp1) > int(temp3):    # Else if age of pilot is less than the MAX age or if age of pilot is more than the MIN age 
            raise EmployeeAgeError
        if self.nid in self.verify_pilot_helper("nid"):     # Checks if nid already exists
            raise EmployeeSsidExistsError
        else:
            return True

    def Rank(self):
        """ Verifies that a pilot's rank is either pilot or copilot
        """

        if self.rank.lower() != "captain" and self.rank.lower() != "copilot":
            raise EmployeeRankError
        else:
            return True

    def License(self): #IMPLEMENT SOMETIME D:
        """ Meant to check if a pilots license is for a plane
            that NaN-Air owns or something, unsure of best implementation
        """
        

    def validatepilot(self):
        self.Ssid()
        self.Name()
        self.Rank()
        self.Address()
        self.PhoneNumber()
        if self.home_phone != "":
            self.HomePhoneNumber()
        self.License()


