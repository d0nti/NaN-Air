import csv

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

      