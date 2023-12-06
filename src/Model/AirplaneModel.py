class Airplane:
    def __init__(self, name = None, plane_type = None, supplier = None, seats = None):
        self.name = name
        self.plane_type = plane_type
        self.supplier = supplier
        self.seats = seats


    def ___str__(self):
        return f"{self.name} {self.plane_type} {self.supplier} {self.seats}"

