from Model.EmployeeModel import Pilot, FlightAttendant
import csv
import os
import io


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
                        row["home_phone_nr"],
                        row["license"],
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
                            row["home_phone_nr"],
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
                            row["home_phone_nr"],
                            row["license"]
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
                            row["home_phone_nr"]
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
                            row["home_phone_nr"]
                        )
                    )
        return heads_of_service

    def register_pilot(self, employee: Pilot):
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
                "home_phone_nr"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvfile.seek(0, io.SEEK_END)
            if csvfile.tell() == 0:
                # we have an empty file so write headers
                writer.writeheader()
            writer.writerow(
                {
                    "nid": employee.nid,
                    "name": employee.name,
                    "role": employee.role,
                    "rank": employee.rank,
                    "license": employee.license,
                    "address": employee.address,
                    "phone_nr": employee.phone_nr,
                    "home_phone_nr": employee.home_phone_nr,
                }
            )

    def register_flight_attendant(self, employee: FlightAttendant):
        with open(self.file_name, "a", encoding="utf-8") as csvfile:
            fieldnames = [
                "nid",
                "name",
                "role",
                "rank",
                "license",
                "address",
                "phone_nr",
                "home_phone_nr",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvfile.seek(0, io.SEEK_END)
            if csvfile.tell() == 0:
                # we have an empty file so write headers
                writer.writeheader()
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
                    "home_phone_nr": employee.home_phone_nr,
                }
            )

    def search_employee(self, filter: str):
        # takes a input from ui and searches for it in the csv file
        matching_employee_list = []
        all_employees = self.get_all_employees()
        for employee in all_employees:
            if employee.license != None and employee.license != "":
                if filter in employee.name or filter in employee.nid or filter in employee.role or filter in employee.rank or filter in employee.license:
                    matching_employee_list.append(employee)
            else:
                if filter in employee.name or filter in employee.nid or filter in employee.role or filter in employee.rank:
                    matching_employee_list.append(employee)

        # returns a list of employee objects that match the search
        return matching_employee_list

    def update_pilot(self, employee_info: Pilot):
        """ Does not replace data yet, 
        """
        allemployees = self.get_all_employees()
        original_file_name = self.file_name
        self.file_name += ".tmp"
        for employee in allemployees:
            if employee.nid == employee_info.nid:
            # Updates new data if edited employee was a pilot
                self.register_pilot(employee_info)
            else:
            # Copies old data to new file
                if employee.license == "N/A": # If employee == FlightAttendant
                    self.register_flight_attendant(employee)
                else:
                    self.register_pilot(employee)
        # Deleting the original .csv file
        os.remove(original_file_name)
        os.rename(self.file_name, original_file_name)
        self.file_name = original_file_name

    def update_flight_attendant(self, employee_info: FlightAttendant):
        """ Does not replace data yet, 
        """
        allemployees = self.get_all_employees()
        original_file_name = self.file_name
        self.file_name += ".tmp"
        for employee in allemployees:
            if employee.nid == employee_info.nid:
            # Updates new data if edited employee was a flight attendant
                self.register_flight_attendant(employee_info)
            else:
            # Copies old data to new file
                if employee.license == "N/A": # If employee == FlightAttendant
                    self.register_flight_attendant(employee)
                else:
                    self.register_pilot(employee)
        # Deleting the original .csv file
        os.remove(original_file_name)
        os.rename(self.file_name, original_file_name)
        self.file_name = original_file_name

    def get_shift_plan(self):
        shift_plan = []
        with open("src/Files/shift_plan.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                shift_plan.append((row["nid"], row["name"], row["shift_start_date"], row["shift_start_time"], row["shift_end_date"], row["shift_end_time"]))

        return shift_plan
    
    def search_by_working_on_day(self, filter: str):
        employees_working = []
        with open("src/Files/shift_plan.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if str(filter) == row["shift_start_date"]:
                    employees_working.append(row)
        return employees_working
    
    def search_by_not_working_on_day(self, filter_date: str):
        employees_not_working = []
        with open("src/Files/shift_plan.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            working_employees = {row["name"] for row in reader if str(filter_date) == row["shift_start_date"]}

            csvfile.seek(0)
            next(reader)

            employees_not_working = [row for row in reader if row["name"] not in working_employees]

        return employees_not_working
    
