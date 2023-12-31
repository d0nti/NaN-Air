from Model.AirplaneModel import Airplane

class InvalidInsigniaCharacterError(Exception):
    pass
class InsigniaFormatError(Exception):
    pass
class InsigniaExistsError(Exception):
    pass


class VerifyAirplane:
    def __init__(self, airplane_info: Airplane, all_airplane_data: list[Airplane]):

        self.all_airplane_data = all_airplane_data
        self.airplane_info = airplane_info

    def verify_airplane_helper(self, info_type: str):
        """ info_type must be a string with the values 'insignia', 'plane_type', 'supplier', 'seats'.
            This func will then return a list of all registered strings 
        """

        in_use_info = []

        for i in range(len(self.all_airplane_data)):
            in_use_info.append(getattr(self.all_airplane_data[i], info_type))    # getattr kallar á method 'info_type' í classa temp

        return in_use_info

    def verify_insignia(self):

        insignia = self.airplane_info.insignia.split("-")
        
        if list(self.airplane_info.insignia)[2] != "-":
            raise InsigniaFormatError()

        elif len(insignia) != 2:
            raise InsigniaFormatError()

        elif len(insignia[0]) != 2:
            raise InsigniaFormatError()

        elif len(insignia[-1]) != 3:
            raise InsigniaFormatError()
        
        elif not insignia[0].isdigit():
            raise InvalidInsigniaCharacterError

        elif not insignia[-1].isdigit():
            raise InvalidInsigniaCharacterError

        elif self.airplane_info.insignia in self.verify_airplane_helper("insignia"):
            raise InsigniaExistsError()

    def validate_plane(self):
        self.verify_insignia()

