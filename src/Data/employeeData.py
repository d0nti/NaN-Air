from Model.EmployeeModel import Pilot, FlightAttendant

import csv


class EmployeeData:
    def __init__(self):
        self.file_name = "src/Files/crew.csv"
        self.shift_file = "src/Files/shift_plan.csv"
        self.number_of_employees = 0

    # frá fyrirlestri
    def get_all_employees(self):
        all_employees = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                all_employees.append(
                    Pilot(
                        row["nid"],
                        row["name"],
                        row["role"],
                        row["rank"],
                        row["address"],
                        row["phone_nr"],
                    )
                )

        return all_employees

    def sort_by_captains(self):
        captains = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["rank"] == "Captain":
                    captains.append(
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
        return captains

    def sort_by_co_pilots(self):
        co_pilots = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["rank"] == "Copilot":
                    co_pilots.append(
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
        return co_pilots


    def sort_by_flight_attendants(self):
        flight_attendants = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["rank"] == "Flight Attendant":
                    flight_attendants.append(
                        FlightAttendant(
                            row["nid"],
                            row["name"],
                            row["role"],
                            row["rank"],
                            row["address"],
                            row["phone_nr"],
                        )
                    )
        return flight_attendants

    def sort_by_heads_of_service(self):
        heads_of_service = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["rank"] == "Flight Service Manager":
                    heads_of_service.append(
                        FlightAttendant(
                            row["nid"],
                            row["name"],
                            row["role"],
                            row["rank"],
                            row["address"],
                            row["phone_nr"],
                        )
                    )
        return heads_of_service

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
        search_result = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (
                    filter in row["name"]
                    or filter in row["nid"]
                    or filter in row["role"]
                    or filter in row["license"]
                ):  # can use these param to search
                    search_result.append(row)
        # returns the list of employees that match the search
        return search_result
    
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
        shift_plan = []
        with open("src/Files/shift_plan.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                shift_plan.append((row["nid"], row["name"], row["shift_start_date"], row["shift_start_time"], row["shift_end_date"], row["shift_end_time"]))

        return shift_plan
    
    def search_by_working_on_day(self, filter):
        employees_working = []
        with open("src/Files/shift_plan.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if str(filter) == row["shift_start_date"]:
                    employees_working.append(row)
        return employees_working
    
    def search_by_not_working_on_day(self, filter_date):
        employees_not_working = []
        with open("src/Files/shift_plan.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            working_employees = {row["name"] for row in reader if str(filter_date) == row["shift_start_date"]}

            csvfile.seek(0)
            next(reader)

            employees_not_working = [row for row in reader if row["name"] not in working_employees]

        return employees_not_working
    
