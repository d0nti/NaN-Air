from Model.DestinationModel import Destination

import csv

class DestinationData:
    def __init__(self):
        self.file_name = "src/Files/destinations.csv"

#frá fyrirlestri
    def get_all_destinations(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile: 
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.number_of_employees += 1
                ret_list.append(Destination(row["name"], row["country"], row["airport"], row["flight_time"], row["distance_from_Iceland"], row["contact_name"], row["contact_phone_nr"]))
            
            return ret_list


    def create_destination(self, destination):
        with open(self.file_name, "a") as csvfile:
            fieldnames = ["name", "country", "airport", "flight_time", "distance_from_Iceland", "contact_name", "contact_phone_nr"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"name": destination.name, "country": destination.country, "airport": destination.airport, "flight_time": destination.flight_time, "distance_from_Iceland": destination.distance_from_Iceland, "contact_name": destination.contact_name, "contact_phone_nr": destination.contact_phone_nr})