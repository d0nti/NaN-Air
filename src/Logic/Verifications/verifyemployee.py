class EmployeeSsidLenError(Exception):
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
MIN_EMP_NAME_LEN = 10

MAX_PILOT_BIRTH_YEAR = "1958"
MAX_PILOT_BIRTH_YEAR = list(MAX_PILOT_BIRTH_YEAR)
MIN_PILOT_BIRTH_YEAR = "1998"
MIN_PILOT_BIRTH_YEAR = list(MIN_PILOT_BIRTH_YEAR)



class VerifyPilot:
    def __init__(self, employee_info):
        """ verification class with methods to verify every input from user when
            creating a new pilot employee.
            Meant to take in an employee class object.
        """
        self.nid = employee_info.nid
        self.name = employee_info.name
        self.role = employee_info.role
        self.rank = employee_info.rank
        self.address = employee_info.address
        self.phone_nr = employee_info.phone_nr
        self.home_phone = employee_info.home_phone_nr
        self.license = employee_info.license

    def Ssid(self):
        """ Checks if ssid is of length 10, checks if ssid is only numbers,
            checks if pilot is older than 65 years or younger than 25,
        """
        temp1 = list(self.nid)
        temp1 = temp1[4:6]
        temp1 = str(temp1[0]) + str(temp1[-1])

        temp2 = MAX_PILOT_BIRTH_YEAR[1:3]
        temp2 = str(temp2[0]) + str(temp2[-1])

        temp3 = MIN_PILOT_BIRTH_YEAR[1:3]
        temp3 = str(temp3[0]) + str(temp3[-1])


        if len(self.nid) != 10:
            raise SsidNumError
        elif not self.nid.isdigit():
            raise SsidNumError
        elif int(temp1) < int(temp2) or int(temp1) > int(temp3):
            raise EmployeeAgeError
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
        if self.rank.lower() != "pilot" or self.rank.lower() != "copilot":
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
        """ Checks that a phone number is 10 digits long
            and that all but the first item are digits
        """
        if len(self.phone_nr) != 10:
            raise EmployeePhoneNumberError
        elif self.phone_nr.split()[0] != "+":
            raise EmployeePhoneNumberError
        elif not self.phone_nr.split()[1:-1].isdigit():
            raise EmployeePhoneNumberError
        else:
            return True


    def HomePhoneNumber(self):
        """ Checks that a home phone number is 10 digits long
            and that all but the first item are digits
        """
        if len(self.home_phone) != 10:
            raise EmployeeHomePhoneNumberError
        elif self.home_phone.split()[0] != "+":
            raise EmployeeHomePhoneNumberError
        elif not self.home_phone.split()[1:-1].isdigit():
            raise EmployeeHomePhoneNumberError
        else:
            return True

    def License(self): #IMPLEMENT SOMETIME D:
        """ Meant to check if a pilots license is for a plane
            that NaN-Air owns or something, unsure of best implementation
        """
        pass

    def CallFunctions(self):
        self.Ssid()
        self.Name()
        self.Rank()
        self.Address()
        self.PhoneNumber()
        self.HomePhoneNumber()
        self.License()



class VerifyFlightAttendant:
    def __init__(self, employee_info):
        """ verification class with methods to verify every input from user when
            creating a new flight attendant employee.
            Meant to take in an employee class object.
        """
        self.nid = employee_info.nid
        self.name = employee_info.name
        self.role = employee_info.role
        self.rank = employee_info.rank
        self.address = employee_info.address
        self.phone_nr = employee_info.phone_nr
        self.home_phone = employee_info.home_phone_nr


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
        # elif int(temp1) < MAX_PILOT_BIRTH_YEAR[-3:-1] or int(temp1) > MIN_PILOT_BIRTH_YEAR[-3:-1]:
        #     raise EmployeeAgeError
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
        
        if self.rank.lower().strip() != "flight attendant" and self.rank.lower().strip() != "flight service manager":
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
        """ Checks that a phone number is 10 digits long
            and that all but the first item are digits
        """
        
        temp = list(self.phone_nr)
        temp2 = ""
        
        for i in range(1, len(temp)):
            temp2 += str(temp[i])


        if len(self.phone_nr) != 11:
            raise EmployeePhoneNumberError
        elif temp[0] != "+":
            raise EmployeePhoneNumberError
        elif not temp2.isdigit():
            raise EmployeePhoneNumberError
        else:
            return True


    def HomePhoneNumber(self):
        """ Checks that a home phone number is 10 digits long
            and that all but the first item are digits
        """
        if len(self.home_phone) != 10:
            raise EmployeeHomePhoneNumberError
        elif self.home_phone.split()[0] != "+":
            raise EmployeeHomePhoneNumberError
        elif not self.home_phone.split()[1:-1].isdigit():
            raise EmployeeHomePhoneNumberError
        else:
            return True


    def CallFunctions(self):
        self.Ssid()
        self.Name()
        self.Rank()
        self.Address()
        self.PhoneNumber()
        if self.home_phone != None:
            self.HomePhoneNumber()
    