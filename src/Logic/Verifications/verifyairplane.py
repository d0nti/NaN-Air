


class VerifyAirplane:
    def __init__(self, airplane_info, data):

        self.data = data
        self.insignia = airplane_info.insignia
        self.plane_type = airplane_info.plane_type
        self.supplier = airplane_info.supplier
        self.seats = airplane_info.seats


    def Verify_Airplane_Helper(self, info_type):
        """ info_type must be a string with the values .
            This func will then return a list of all registered strings 
        """

        in_use_info = []

        for i in range(len(self.data)):
            temp = self.data[i]
            in_use_info.append(temp.get(str(info_type)))

        return in_use_info


    def verify_insignia(self):

        insignia = self.insignia.split("-")

        if len(insignia) != 2:
            pass#ERROR

        elif len(insignia[0]) != 2:
            pass#ERROR

        elif len(insignia[-1]) != 3:
            pass#ERROR


    def verify_plane_type(self):

        if self.plane_type not in self.Verify_Airplane_Helper(""):
            pass
