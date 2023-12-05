import csv

class PlaneData:
    def __init__(self):
        self.file_name = "src/Files/airplanes.csv"

    def get_all_airplanes(self):
        with open(self.file_name, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            airplanes_dict = [row for row in reader]
            return airplanes_dict

    def create_airplane(self, plane):
        with open(self.file_name, "a", encoding="utf-8") as csv_file:
            fieldnames = ["name", "type", "supplier", "seats"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            employee_data = list(map(lambda key: plane[key], plane.keys()))
            writer.writerow({"name": employee_data[0], "type": employee_data[1], "supplier": employee_data[2], "seats": employee_data[3]})