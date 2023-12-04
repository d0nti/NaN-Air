class Employee:
    def __init__(self, name="", ssid=""):
        self.name = name
        self.ssid = ssid

    def __str__(self):
        return f"name: {self.name}, SSID: {self.ssid}"