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
                ret_list.append(
                    Voyage(
                        row["vid"],
                        row["destination"],
                        row["departuretime"],
                        row["departuredate"],
                        row["arrivaltime"],
                        row["arrivaldate"],
                        row["captain"],
                        row["copilot"],
                        row["flight_service_manager"],
                        row["flight_attendant"],
                    )
                )
            return ret_list

    def register_new_voyage(self, voyage):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "vid",
                "destination",
                "departuretime",
                "departuredate",
                "arrivaltime",
                "arrivaldate",
                "captain",
                "copilot",
                "flight_service_manager",
                "flight_attendant",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(
                {
                    "vid": voyage[0],
                    "destination": voyage[1],
                    "departuretime": voyage[2],
                    "departuredate": voyage[3],
                    "arrivaltime": voyage[4],
                    "arrivaldate": voyage[5],
                    "captain": voyage[6],
                    "copilot": voyage[7],
                    "flight_service_manager": voyage[8],
                    "flight_attendant": voyage[9],
                }
            )

    def search_voyages(self, filter):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if filter in row["vid"] or filter in row["destination"]:
                    ret_list.append(row)
        return ret_list
    
    def copy_voyage(self, voyage):
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if voyage == row["vid"]:
                    self.register_new_voyage(row)
                    

