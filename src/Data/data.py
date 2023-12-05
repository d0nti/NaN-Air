import csv

class EmployeeData:
    def __init__(self):
        self.file_name = "src/Files/employees.csv"
        

    def get_all_employees(self):
        with open(self.file_name, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            employees_dict = [row for row in reader]
            return employees_dict


    def create_employee(self, employee):
        with open(self.file_name, "a", encoding="utf-8") as csv_file:
            fieldnames = ["name", "ssid", "job title", "license", "address", "phone_number", "e_mail_address", "home_phone"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            employee_data = list(map(lambda key: employee[key], employee.keys()))
            writer.writerow({"name": employee_data[0], "ssid": employee_data[1], "job title": employee_data[2], "license": employee_data[3], "address": employee_data[4], "phone_number": employee_data[5], "e_mail_address": employee_data[6], "home_phone": employee_data[7]})




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

class DestinationData:
    def __init__(self):
        self.file_name = "src/Files/Destinations.csv"

    def get_all_destinations(self):
        with open(self.file_name, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            destination_dict = [row for row in reader]
            return destination_dict

    def create_destination(self, destination):
        with open(self.file_name, "a", encoding="utf-8") as csv_file:
            fieldnames = ["name", "country", "airport", "flight_time", "distance_from_Iceland", "contact_name", "contact_phone_nr"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            DestinationData = list(map(lambda key: destination[key], destination.keys()))
            writer.writerow({"name": DestinationData[0], "country": DestinationData[1], "airport": DestinationData[2], "flight_time": DestinationData[3], "distance_from_Iceland": DestinationData[4], "contact_name": DestinationData[5], "contact_phone_nr": DestinationData[6]})

      