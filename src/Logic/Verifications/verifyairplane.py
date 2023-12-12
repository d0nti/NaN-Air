


class VerifyAirplane:
    def __init__(self, airplane_info, data):
        
        self.insignia = airplane_info.insignia
        self.plane_type = airplane_info.plane_type
        self.supplier = airplane_info.supplier
        self.seats = airplane_info.seats

    def verify_insignia(self):
        
        insignia = self.insignia.split("-")

        if len(insignia) != 2:
            pass#ERROR

        elif len(insignia[0]) != 2:
            pass#ERROR
        
        elif len(insignia[-1]) != 3:
            pass#ERROR



    def verify_plane_type(self):
        plane_type 
