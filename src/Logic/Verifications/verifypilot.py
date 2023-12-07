class EmployeeSsidLenError:
    pass
class SsidNumError:
    pass
class EmployeeAgeError:
    pass
class EmployeeNameLongError:
    pass
class EmployeeNameShortError:
    pass
class EmployeeRoleError:
    pass
class EmployeeRankError:
    pass
class EmployeeAddressError:
    pass
class EmployeePhoneNumberError:
    pass
class EmployeeHomePhoneNumberError:
    pass
class PilotLicenseError:
    pass


MAX_EMP_NAME_LEN = 100
MIN_EMP_NAME_LEN = 10


class VerifyPilot:
    def __init__(self, employee_info):
        """ verification class with methods to verify every input from user when
            creating a new pilot employee.
            Meant to take in an employee class object.
        """
        self.ssid = employee_info.ssid
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
        if len(self.ssid) != 10:
            raise SsidNumError
        elif not self.ssid.isdigit():
            raise SsidNumError
        elif self.ssid.split()[4:5] < 58 or self.ssid.split()[4:5] > 98:
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
            raise EmployeeRoleError
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

