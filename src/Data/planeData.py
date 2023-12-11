from Model.AirplaneModel import Airplane
from Model.DestinationModel import Destination

import csv

class AirplaneData:
    def __init__(self):
        """ Designates two filenames, the former is a file containing NaN-Air owned aircrafts,
            the latter is a file containing details on aircrafts that exist, which will be
            used to assign NaN-Air planes the correct details, mainly the number of seats
            they contain and the manufacturer of the airplane.
        """
        self.plane_file_name = "src/Files/aircraft.csv"
        self.legal_plane_file_name = "src/Files/aircraft_type.csv"


    def get_all_airplanes(self):
        """ Opens the file containing NaN-Air owned aircrafts and takes their names and type id
            and adds to the Airplane class.
        """
        ret_list = []
        with open(self.plane_file_name, newline="", encoding="utf-8") as file:
            file_reader = csv.DictReader(file)
            for item in file_reader:
                ret_list.append(Airplane(item["plane_insignia"], item["plane_type_id"]))
            
            self.get_all_airplanes_helper(ret_list)
            return ret_list


    def get_all_airplanes_helper(self, ret_list):
        with open(self.legal_plane_file_name, newline="", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            rows = list(csv_reader)
            print(rows)

            for i in range(len(ret_list)):
                
                if ret_list[i].plane_type == "NABAE146":
                    ret_list[i].plane_type = rows[0].get("plane_type_id")
                    ret_list[i].supplier = rows[0].get("manufacturer")
                    ret_list[i].seats = rows[0].get("capacity")

                elif ret_list[i].plane_type == "NAFokkerF28":
                    ret_list[i].plane_type = rows[1].get("plane_type_id")
                    ret_list[i].supplier = rows[1].get("manufacturer")
                    ret_list[i].seats = rows[1].get("capacity")

                elif ret_list[i].plane_type == "NAFokkerF100":
                    ret_list[i].plane_type = rows[2].get("plane_type_id")
                    ret_list[i].supplier = rows[2].get("manufacturer")
                    ret_list[i].seats = rows[2].get("capacity")

                else:
                    print("wtf")


#aircraft.csv
#plane_insignia,plane_type_id,date_of_manufacture,last_maintenance
#aircraft_type.csv
#plane_type_id,manufacturer,model,capacity,empty_weight,max_takeoff_weight,unit_thrust,service_ceiling,length,height,wingspan


    def create_airplane(self, plane):
        with open(self.plane_file_name, "a", encoding="utf-8") as csv_file:
            fieldnames = ["name", "type", "supplier", "seats"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            employee_data = list(map(lambda key: plane[key], plane.keys()))
            writer.writerow({"name": employee_data[0], "type": employee_data[1], "supplier": employee_data[2], "seats": employee_data[3]})



            #frá fyrirlestri
    def get_all_destinations(self):
        ret_list = []
        with open(self.plane_file_name, newline="", encoding="utf-8") as csvfile: 
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.number_of_employees += 1
                ret_list.append(Destination(row["name"], row["country"], row["airport"], row["flight_time"], row["distance_from_Iceland"], row["contact_name"], row["contact_phone_nr"]))
            
            return ret_list


    def create_destination(self, destination):
        with open(self.plane_file_name, "a") as csvfile:
            fieldnames = ["name", "country", "airport", "flight_time", "distance_from_Iceland", "contact_name", "contact_phone_nr"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"name": Destination.name, "country": Destination.country, "airport": destination.airport, "flight_time": destination.flight_time, "distance_from_Iceland": destination.distance_from_Iceland, "contact_name": destination.contact_name, "contact_phone_nr": destination.contact_phone_nr})