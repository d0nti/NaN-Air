from Model.DestinationModel import Destination

import csv
import io
import os


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

    def register_destination(self, destination):
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
            csvfile.seek(0, io.SEEK_END)
            if csvfile.tell() == 0:
                # we have an empty file so write headers
                writer.writeheader()

            writer.writerow(
                {
                    "name": destination.name,
                    "country": destination.country,
                    "airport": destination.airport,
                    "flight_time": destination.flight_time + "_hour",
                    "distance_from_Iceland": destination.distance_from_Iceland + "km",
                    "contact_name": destination.contact_name,
                    "contact_phone_nr": destination.contact_phone_nr,
                }
            )

    def search_destination(self, filter):
        searched_destination = []

        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (
                    filter in row["name"]
                    or filter in row["country"]
                    or filter in row["airport"]
                    or filter in row["flight_time"]
                    or filter in row["distance_from_Iceland"]
                    or filter in row["contact_name"]
                    or filter in row["contact_phone_nr"]
                ):
                    searched_destination.append(
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
                return searched_destination

    def update_destination(self, destination: Destination):
        """This function takes in uppdated instance of Destination.
        In order to do this it must read all, write all back with one istance changed
        For safety a temp file is created so no file can be lost
        """
        # We need to:
        #  a)  read all
        #  b)  for all
        #  c)  write old or updated if the one to change
        #  d)  delete old if write is ok
        #  e)  rename temp file to correct file name

        alldest = self.get_all_destinations()
        filename_org = self.file_name
        self.file_name += ".tmp"
        for dest in alldest:
            if dest.name == destination.name:
                # here we updaet the new date
                self.register_destination(destination)
            else:
                # copy old data to new file
                self.register_destination(dest)
        # delete the original .csv file
        os.remove(filename_org)
        # rename the .csv.tmp to .csv
        os.rename(self.file_name, filename_org)
        # change the instnace filename back as it was
        self.file_name = filename_org
