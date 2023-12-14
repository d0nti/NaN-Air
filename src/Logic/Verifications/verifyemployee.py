from Model.EmployeeModel import Employee, Pilot, FlightAttendant

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
class EmployeeRoleError(Exception):
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
    def __init__(self, employee_info: FlightAttendant, all_employee_data: list[Employee]):
        """ verification class with methods to verify every input from user when
            creating a new flight attendant employee.
            Meant to take in an employee class object.
        """
        self.employee_info = employee_info
        self.all_employee_data = all_employee_data


    def verify_flight_attendant_helper(self, info_type: str):
        """ info_type must be a string with the values 'nid', 'name', 'role',
            'rank', 'address', 'phone_nr', 'home_phone_nr' or 'license'.
            This func will then return a list of all registered strings 
        """
        info_in_use = []

        for i in range(len(self.all_employee_data)):
            index_data = self.all_employee_data[i]
            info_in_use.append(getattr(index_data, info_type))

        return info_in_use


    def Ssid(self):
        """ Checks if ssid is of length 10, checks if ssid is only numbers,
            checks if pilot is older than 65 years or younger than 25,
        """
        temp1 = list(self.employee_info.nid)
        temp1 = temp1[4:6]
        temp1 = str(temp1[0]) + str(temp1[-1])

        if len(self.employee_info.nid) != 10:
            raise SsidNumError
        elif not self.employee_info.nid.isdigit():
            raise SsidNumError
        if self.employee_info.nid in self.verify_flight_attendant_helper("nid"):     # Checks if nid already exists
            raise EmployeeSsidExistsError
        else:
            return True


    def Name(self):
        """ Checks if a pilot's name is longer than MAX_EMP_NAME_LEN
            or shorter than MIN_EMP_NAME_LEN
        """
        if len(self.employee_info.name) > MAX_EMP_NAME_LEN:
            raise EmployeeNameLongError
        elif len(self.employee_info.name) < MIN_EMP_NAME_LEN:
            raise EmployeeNameShortError
        else:
            return True

    def Role(self):
        """
        """
        if self.employee_info.role.lower() != "cabincrew":
            raise EmployeeRoleError
        else:
            return True


    def Rank(self):
        """ Verifies that a pilot's rank is either pilot or copilot
        """
        if self.employee_info.rank.lower() != "flight attendant" and self.employee_info.rank.lower() != "flight service manager":
            raise EmployeeRankError
        else:
            return True


    def Address(self):
        """ Splits the address string into a list and verifies that the first 
            item is not digits and that the last item is digits
        """
        temp = self.employee_info.address.split(" ")
        
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
        if len(str(self.employee_info.phone_nr)) != 7:
            raise EmployeePhoneNumberError
        if not str(self.employee_info.phone_nr).isdigit():
            raise EmployeePhoneNumberError
        else:
            return True


    def HomePhoneNumber(self):
        """ Checks that a home phone number is 11 digits long
            and that all but the first item are digits
        """
        if len(str(self.employee_info.home_phone)) != 7:
            raise EmployeeHomePhoneNumberError
        if not str(self.employee_info.phone_nr).isdigit():
            raise EmployeeHomePhoneNumberError
        else:
            return True

    def validateflightattendant(self):
        self.Ssid()
        self.Name()
        self.Rank()
        self.Address()
        self.PhoneNumber()
        if self.employee_info.home_phone_nr != "":
            self.HomePhoneNumber()
    


class VerifyPilot(VerifyFlightAttendant):
    def __init__(self, employee_info: Pilot, all_employee_info: list[Employee]):
        """ verification class with methods to verify every input from user when
            creating a new pilot employee.
            Meant to take in an employee class object.
        """
        self.all_employee_info = all_employee_info
        self.employee_info = employee_info


    def verify_pilot_helper(self, info_type: str):
        """ info_type must be a string with the values 'nid', 'name', 'role',
            'rank', 'address', 'phone_nr', 'home_phone_nr' or 'license'.
            This func will then return a list of all registered strings 
        """
        info_in_use = []

        for i in range(len(self.all_employee_info)):
            index_data = self.all_employee_info[i]
            info_in_use.append(getattr(index_data, info_type))

        return info_in_use


    def Ssid(self):
        """ Checks if ssid is of length 10, checks if ssid is only numbers,
            checks if pilot is older than 65 years or younger than 25,
        """

        temp1 = list(self.employee_info.nid)                  # Transform nid to a list data type for later indexing
        temp1 = temp1[4:6]                      # Takes the "age" numericals from ssid and assigns them to temp1 
        temp1 = str(temp1[0]) + str(temp1[-1])  # Splices both numericals from the line above into a string and assigns them to temp1

        temp2 = MAX_PILOT_BIRTH_YEAR[1:3]       # Takes the numerical values needed from MAX_PILOT_BIRTH_YEAR and assigns them to temp2
        temp2 = str(temp2[0]) + str(temp2[-1])  # Splices both numericals from the line above into a string and assigns them to temp2

        temp3 = MIN_PILOT_BIRTH_YEAR[1:3]       # Takes the numerical values needed from MIN_PILOT_BIRTH_YEAR and assigns them to temp3
        temp3 = str(temp3[0]) + str(temp3[-1])  # Splices both numericals from the line above into a string and assigns them to temp3


        if len(self.employee_info.nid) != 10:     # If ssid number is not 10 digits
            raise SsidNumError
        if not self.employee_info.nid.isdigit():    # Else if all numbers in the ssid are not digits
            raise SsidNumError
        if int(temp1) < int(temp2) and int(temp1) > int(temp3):    # Else if age of pilot is less than the MAX age or if age of pilot is more than the MIN age 
            raise EmployeeAgeError
        if self.employee_info.nid in self.verify_pilot_helper("nid"):     # Checks if nid already exists
            raise EmployeeSsidExistsError
        else:
            return True

    def Role(self):
        """
        """
        if self.employee_info.role.lower() != "pilot":
            raise EmployeeRoleError
        else:
            return True

    def Rank(self):
        """ Verifies that a pilot's rank is either pilot or copilot
        """

        if self.employee_info.rank.lower() != "captain" and self.employee_info.rank.lower() != "copilot":
            raise EmployeeRankError
        else:
            return True

    def License(self): #IMPLEMENT SOMETIME D:
        """ Meant to check if a pilots license is for a plane
            that NaN-Air owns or something, unsure of best implementation
        """
        if self.employee_info.license.lower() in self.verify_pilot_helper("license"):
            raise PilotLicenseError
        else:
            return True

    def validatepilot(self):
        self.Ssid()
        self.Name()
        self.Rank()
        self.Address()
        self.PhoneNumber()
        if self.employee_info.home_phone_nr != "":
            self.HomePhoneNumber()
        self.License()


