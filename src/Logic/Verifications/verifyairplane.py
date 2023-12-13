class InvalidInsigniaError(Exception):
    pass
class InsigniaFormatError(Exception):
    pass
class InsigniaExistsError(Exception):
    pass


class VerifyAirplane:
    def __init__(self, airplane_info, data):

        self.data = data
        self.insignia = airplane_info.insignia


    def verify_airplane_helper(self, info_type: str):
        """ info_type must be a string with the values 'insignia', 'plane_type', 'supplier', 'seats'.
            This func will then return a list of all registered strings 
        """

        in_use_info = []

        for i in range(len(self.data)):
            temp = self.data[i]
            in_use_info.append(getattr(temp, info_type))    # getattr kallar á method 'info_type' í classa temp

        return in_use_info


    def verify_insignia(self):

        insignia = self.insignia.split("-")
        
        if self.insignia.split()[2] != "-":
            raise InsigniaFormatError()

        elif len(insignia) != 2:
            raise InsigniaFormatError()

        elif len(insignia[0]) != 2:
            raise InsigniaFormatError()

        elif len(insignia[-1]) != 3:
            raise InsigniaFormatError()

        elif self.insignia in self.verify_airplane_helper("insignia"):
            raise InsigniaExistsError()


    def validate_plane(self):
        self.verify_insignia()

