from Model.VoyageModel import Voyage

import csv

class VoyageData:
    def __init__(self):
        self.file_name = "src/Files/voyages.csv"
        
    def get_all_voyages(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile: 
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Voyage(row["vid"], row["destination"], row["departuretime"], row["departuredate"], row["arrivaltime"], row["arrivaldate"], row["captain"], row["copilot"], row["flight_service_manager"], row["flight_attendant"]))
            return ret_list
        
    def create_voyage(self, voyage):
        with open(self.file_name, "a") as csvfile:
            fieldnames = ["vid", "destination", "departuretime", "departuredate", "arrivaltime", "arrivaldate", "captain", "copilot", "flight_service_manager", "flight_attendant"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"vid": voyage.vid, "destination": voyage.destination, "departuretime": voyage.departuretime, "departuredate": voyage.departuredate, "arrivaltime": voyage.arrivaltime, "arrivaldate": voyage.arrivaldate, "captain": voyage.captain, "copilot": voyage.copilot, "flight_service_manager": voyage.flight_service_manager, "flight_attendant": voyage.flight_attendant})
            
    