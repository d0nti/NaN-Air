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
        self.ssid = employee.ssid
        self.name = employee.name
        self.role = employee.role
        self.rank = employee.rank
        self.address = employee.address
        self.phone_nr = employee.phone_nr
        self.home_phone = employee.home_phone_nr
        self.license = employee.license

    def Ssid(self):
        """ Checks if ssid is of length 10, checks if ssid is only numbers,
            checks if pilot is older than 65 years or younger than 25,
        """
        if len(self.ssid) == 10:
            if self.ssid.isdigit():
                self.ssid = self.ssid.split()
                if self.ssid[4:5] < 58 or self.ssid[4:5] > 98:
                    return True
                else:
                    raise EmployeeAgeError
            else:
                raise SsidNumError
        else:
            raise EmployeeSsidLenError

    def Name(self):
        if len(self.name) > MAX_EMP_NAME_LEN:
            raise EmployeeNameLongError
        elif len(self.name) < MIN_EMP_NAME_LEN:
            raise EmployeeNameShortError
        else:
            return True

    def Rank(self):
        self.rank = self.rank.lower()
        if self.rank != "pilot" or self.rank != "copilot":
            raise EmployeeRoleError
        else:
            return True

    def Address(self):
        self.address.split()
        if self.address[0].isdigit():
            if not self.address[-1].isdigit():
                raise EmployeeAddressError
            else:
                return True
        else:
            return True
          
    
    def PhoneNumber(self):
        if not self.phone_nr.isdigit():
            raise EmployeePhoneNumberError
        else:
            return True
    
    def HomePhoneNumber(self):
        if not self.home_phone.split()[1:-1].isdigit():
            raise EmployeeHomePhoneNumberError
        else:
            return True
    
    def License(self): #IMPLEMENT SOMETIME D:
        pass

