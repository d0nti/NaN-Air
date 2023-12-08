from Model.EmployeeModel import Employee
from Model.EmployeeModel import Pilot
from Model.EmployeeModel import FlightAttendant

import csv



class EmployeeData:
    def __init__(self):
        self.file_name = "src/Files/crew.csv"
        self.number_of_employees = 0

#from lecture on echo360
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
        with open(self.file_name, "a") as csvfile:
            fieldnames = ["nid", "name", "role", "rank", "address", "phone_nr"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({"nid": employee.nid, "name": employee.name,
                             "role": employee.role, "rank": employee.rank, 
                             "address": employee.address, "phone_nr": employee.phone_nr})


    def update_pilot(self, filter, new_info):
        pilots = self.logic_data_wrapper.search(filter)  #searches for pilots matching the filter
        for pilot in pilots:
            #update pilot info with new_info
            pilot.role = new_info.role
            pilot.rank = new_info.rank
            pilot.license = new_info.license
            pilot.phone_nr = new_info.phone_nr
            pilot.address = new_info.address

        #save updated info
        self.logic_data_wrapper.save_employees(pilots)

    def update_flight_attendant(self, filter, new_info):
        flight_attendants = self.logic_data_wrapper.search(filter) #searches for flight attendants matching the filter
        for flight_attendants in flight_attendants:
            #update flight attendant info with new_info
            flight_attendants.role = new_info.role
            flight_attendants.rank = new_info.rank
            flight_attendants.phone_nr = new_info.phone_nr
            flight_attendants.address = new_info.address
        
        #save updated info
        self.logic_data_wrapper.save_employees(flight_attendants)
