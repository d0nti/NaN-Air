from Model.EmployeeModel import Employee
from Model.EmployeeModel import Pilot
from Model.EmployeeModel import FlightAttendant

import csv


class EmployeeData:
    def __init__(self):
        self.file_name = "src/Files/crew.csv"
        self.shift_file = "src/Files/shift_plan.csv"
        self.number_of_employees = 0

    # frá fyrirlestri
    def get_all_employees(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    Pilot(
                        row["nid"],
                        row["name"],
                        row["role"],
                        row["rank"],
                        row["address"],
                        row["phone_nr"],
                    )
                )

        return ret_list

    def sort_by_captains(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["rank"] == "Captain":
                    ret_list.append(
                        Pilot(
                            row["nid"],
                            row["name"],
                            row["role"],
                            row["rank"],
                            row["address"],
                            row["phone_nr"],
                            row["license"],
                        )
                    )
        return ret_list

    def sort_by_co_pilots(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["rank"] == "Copilot":
                    ret_list.append(
                        Pilot(
                            row["nid"],
                            row["name"],
                            row["role"],
                            row["rank"],
                            row["address"],
                            row["phone_nr"],
                            row["license"],
                        )
                    )
        return ret_list


    def sort_by_flight_attendants(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["rank"] == "Flight Attendant":
                    ret_list.append(
                        FlightAttendant(
                            row["nid"],
                            row["name"],
                            row["role"],
                            row["rank"],
                            row["address"],
                            row["phone_nr"],
                        )
                    )
        return ret_list

    def sort_by_heads_of_service(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["rank"] == "Flight Service Manager":
                    ret_list.append(
                        FlightAttendant(
                            row["nid"],
                            row["name"],
                            row["role"],
                            row["rank"],
                            row["address"],
                            row["phone_nr"],
                        )
                    )
        return ret_list

        # extra_sort = self.get_all_employees()
        # pilot_list = []

        # for employee in extra_sort:
        #     if employee.get('rank') == "Pilot":
        #         pilot_list.append(employee)

        # return pilot_list

    def register_pilot(self, employee):
        """Recieves a list containing information needed for registering a new pilot
        and uses list indexing to assign each value to the correct place
        """
        with open(self.file_name, "a", encoding="utf-8") as csvfile:
            fieldnames = [
                "nid",
                "name",
                "role",
                "rank",
                "license",
                "address",
                "phone_nr",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(
                {
                    "nid": employee.nid,
                    "name": employee.name,
                    "role": employee.role,
                    "rank": employee.rank,
                    "license": employee.license,
                    "address": employee.address,
                    "phone_nr": employee.phone_nr,
                }
            )

    def register_flight_attendant(self, employee):
        with open(self.file_name, "a", encoding="utf-8") as csvfile:
            fieldnames = [
                "nid",
                "name",
                "role",
                "rank",
                "license",
                "address",
                "phone_nr",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(
                {
                    "nid": employee.nid,
                    "name": employee.name,
                    "role": employee.role,
                    "rank": employee.rank,
                    "license": "N/A",
                    "address": employee.address,
                    "phone_nr": employee.phone_nr,
                }
            )

    def search(self, filter):
        # takes a input from ui and searches for it in the csv file
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (
                    filter in row["name"]
                    or filter in row["nid"]
                    or filter in row["role"]
                ):  # can use these param to search
                    ret_list.append(row)
        # returns the list of employees that match the search
        return ret_list

    def get_shift_plan(self):
            ret_list = []
            with open("src/Files/shift_plan.csv", newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    ret_list.append((row["nid"], row["name"], row["shift_start_date"], row["shift_start_time"], row["shift_end_date"], row["shift_end_time"]))

            return ret_list
    
    def search_by_not_day(self, filter):
         ret_list = []
         with open("src/Files/shift_plan.csv", newline="", encoding="utf-8") as csvfile:
             reader = csv.DictReader(csvfile)
             for row in reader:
                 if str(filter) != row["shift_start_date"]:
                     ret_list.append(row)
                 elif str(filter) == row["shift_start_date"]:
                     ret_list = [r for r in ret_list if r["name"] != row["name"]] #if the person is working on that day remove the name from list
         return ret_list 