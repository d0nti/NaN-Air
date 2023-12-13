from Model.DestinationModel import Destination

import csv


class DestinationData:
    def __init__(self):
        self.file_name = "src/Files/Destinations.csv"

    # frá fyrirlestri
    def get_all_destinations(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                ret_list.append(
                    Destination(
                        row["name"],
                        row["country"],
                        row["airport"],
                        row["flight_time"],
                        row["distance_from_Iceland"],
                        row["contact_name"],
                        row["contact_phone_nr"],
                    )
                )

        return ret_list

    def create_destination(self, destination):
        with open(self.file_name, "a", encoding="utf-8") as csvfile:
            fieldnames = [
                "name",
                "country",
                "airport",
                "flight_time",
                "distance_from_Iceland",
                "contact_name",
                "contact_phone_nr",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(
                {
                    "name": destination.name,
                    "country": destination.country,
                    "airport": destination.airport,
                    "flight_time": destination.flight_time,
                    "distance_from_Iceland": destination.distance_from_Iceland,
                    "contact_name": destination.contact_name,
                    "contact_phone_nr": destination.contact_phone_nr,
                }
            )

    def search_destination(self, filter):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (
                    filter in row["name"]
                    or filter in row["airport"]
                    or filter in row["contact_name"]
                    or filter in row["contact_phone_nr"]
                ):
                    ret_list.append(row)
        return ret_list
