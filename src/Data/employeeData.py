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
        with open(self.file_name, "a", encoding="utf-8") as csvfile:
            fieldnames = ["nid", "name", "role", "rank", "license", "phone_nr", "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"nid": employee.nid, "name": employee.name,
                             "role": employee.role, "rank": employee.rank,
                             "license": employee.license, "address": employee.address,
                             "phone_nr": employee.phone_nr})
            

    def register_flight_attendant(self, employee):
        with open(self.file_name, "a", encoding="utf-8") as csvfile:
            fieldnames = ["nid", "name", "role", "rank", "license", "address", "phone_nr"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({"nid": employee.nid, "name": employee.name,
                             "role": employee.role, "rank": employee.rank, "license": "N/A",
                             "address": employee.address, "phone_nr": employee.phone_nr})

#nid,name,role,rank,license,address,phone_nr,pref_nr,slot_param
    def search(self, filter):
        #takes a input from ui and searches for it in the csv file
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if filter in row["name"] or filter in row["nid"] or filter in row["role"] or filter in row ["license"]: #can use these param to search
                    ret_list.append(row)
        #returns the list of employees that match the search
        return ret_list
             

    def delete_employee(self, nid):
        with open(self.file_name, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        # Find the employee with the matching nid
        for i, row in enumerate(rows):
            if row["nid"] == nid:
                # Remove the employee from the list of rows
                del rows[i]
                break

        # Write the updated contents back to the CSV file
        with open(self.file_name, "w", encoding="utf-8") as csvfile:
            fieldnames = ["nid", "name", "role", "rank", "license", "address", "phone_nr", "pref_nr", "slot_param"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

#marvin
#ssid, rank, address, phone_nr, home_phone_nr, license)

    def update_pilot(self, employee):
        # Search for the pilot by nid
        pilots = self.search(employee.nid)

        # If the pilot is found, delete the existing pilot
        if pilots:
            self.delete_employee(pilots[0]["nid"])

        # Register the updated pilot
        self.register_pilot(employee)
        
        