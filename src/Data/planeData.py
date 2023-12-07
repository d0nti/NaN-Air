from Model.AirplaneModel import Airplane

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
        with open(self.plane_file_name, newline = "", encoding = "utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                ret_list.append(Airplane(row["plane_insignia"], row["plane_type_id"]))
                self.get_all_airplanes_helper(ret_list)
            return ret_list

    def get_all_airplanes_helper(self, airplane_list):
        """ Opens the file containing legal aircraft types and adds the missing information
            needed to the list that the 'get_all_airplanes' function was creating.
            This function is meant to be called inside of the other function above.
        """
        with open(self.legal_plane_file_name, newline = "", encoding = "utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            reader.split(",")
            if airplane_list[-1].plane_type == reader[1]:
                airplane_list[-1].supplier = reader[1]
                airplane_list[-1].seats = reader[3]

                

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