class Airplane:
    def __init__(self, insignia = None, plane_type = None, supplier = None, seats = None):
        self.insignia = insignia
        self.plane_type = plane_type
        self.supplier = supplier
        self.seats = seats

    def __str__(self):
        return f"{self.insignia} {self.plane_type} {self.supplier} {self.seats}"