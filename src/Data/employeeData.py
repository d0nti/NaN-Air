from Model.EmployeeModel import Employee
from Model.EmployeeModel import Pilot
from Model.EmployeeModel import FlightAttendant

import csv



class EmployeeData:
    def __init__(self):
        self.file_name = "src/Files/crew.csv"
        self.number_of_employees = 0

#frá fyrirlestri
    def get_all_employees(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile: 
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.number_of_employees += 1
                ret_list.append(Pilot(row["nid"], row["name"], row["role"], row["rank"], row["address"], row["phone_nr"]))

            return ret_list


    def sort_by_captains(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.number_of_employees += 1
                if row["rank"] == "Captain":
                    ret_list.append(Pilot(row["nid"], row["name"], row["role"], row["rank"], row["address"], row["phone_nr"], row["license"]))
            return ret_list
        
        
    def sort_by_co_pilots(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.number_of_employees += 1
                if row["rank"] == "Copilot":
                    ret_list.append(Pilot(row["nid"], row["name"], row["role"], row["rank"], row["address"], row["phone_nr"], row["license"]))
        return ret_list
    
    def sort_by_flight_attendants(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.number_of_employees += 1
                if row["rank"] == "Flight Attendant":
                    ret_list.append(FlightAttendant(row["nid"], row["name"], row["role"], row["rank"], row["address"], row["phone_nr"]))
        return ret_list

    def sort_by_heads_of_service(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.number_of_employees += 1
                if row["rank"] == "Flight Service Manager":
                    ret_list.append(FlightAttendant(row["nid"], row["name"], row["role"], row["rank"], row["address"], row["phone_nr"]))
        return ret_list


        # extra_sort = self.get_all_employees()
        # pilot_list = []

        # for employee in extra_sort:
        #     if employee.get('rank') == "Pilot":
        #         pilot_list.append(employee)

        # return pilot_list




    def register_pilot(self, employee):
        """ Recieves a list containing information needed for registering a new pilot
            and uses list indexing to assign each value to the correct place
        """
        with open(self.file_name, "a") as csvfile:
            fieldnames = ["nid", "name", "role", "rank", "license","phone_nr", "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"nid": employee.nid, "name": employee.name,
                             "role": employee.role, "rank": employee.rank,
                             "license": employee.licence, "address": employee.address,
                             "phone_nr": employee.phone_nr})
            

    def register_flight_attendant(self, employee):
        with open(self.file_name, "a", encoding="utf-8") as csvfile:
            fieldnames = ["nid", "name", "role", "rank", "address", "phone_nr"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({"nid": employee.nid, "name": employee.name,
                             "role": employee.role, "rank": employee.rank, 
                             "address": employee.address, "phone_nr": employee.phone_nr})





