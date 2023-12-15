class Airplane:
    def __init__(self, insignia: str = None, plane_type: str = None, supplier: str = None, seats: int = None):
        self.insignia = insignia
        self.plane_type = plane_type
        self.supplier = supplier
        self.seats = seats

    def __str__(self):
        return f"{self.insignia} {self.plane_type} {self.supplier} {self.seats}"