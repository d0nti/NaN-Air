from Model.EmployeeModel import Pilot, FlightAttendant

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

    def search_employee(self, filter):
        # takes a input from ui and searches for it in the csv file
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (
                    filter in row["name"]
                    or filter in row["nid"]
                    or filter in row["role"]
                    or filter in row["license"]
                ):  # can use these param to search
                    ret_list.append(row)
        # returns the list of employees that match the search
        return ret_list
    
    def update_pilot(self, employee_info: dict):
        """ Does not replace data yet, 
        """
        with open(self.file_name, "w", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["nid"] == employee_info["nid"]:
                    for i in employee_info:
                        if i != "" and i != None:
                            row[employee_info[i]] = i

    def get_shift_plan(self):
        ret_list = []
        with open("src/Files/shift_plan.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append((row["nid"], row["name"], row["shift_start_date"], row["shift_start_time"], row["shift_end_date"], row["shift_end_time"]))

        return ret_list
    
    def search_by_day(self, filter):
        ret_list = []
        with open("src/Files/shift_plan.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if str(filter) == row["shift_start_date"]:
                    ret_list.append(row)
        return ret_list
    
    def search_by_not_day(self, filter_date):
        with open("src/Files/shift_plan.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            working_employees = {row["name"] for row in reader if str(filter_date) == row["shift_start_date"]}

            csvfile.seek(0)
            next(reader)

            ret_list = [row for row in reader if row["name"] not in working_employees]

        return ret_list
    
