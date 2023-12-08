class AirplaneCrust:
    def __init__(self, insignia = None, plane_type = None, supplier = None, seats = None):
        self.insignia = insignia
        self.plane_type = plane_type
        self.supplier = supplier
        self.seats = seats

    def ___str__(self):
        return f"{self.insignia} {self.plane_type} {self.supplier} {self.seats}"

class AirplaneMeat(AirplaneCrust):
    def __init__(self, insignia = None, plane_type = None, supplier = None, seats = None):
        self.plane_type = plane_type
        self.supplier = supplier
        self.seats = seats
        super().__init__(insignia)

