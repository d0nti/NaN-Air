from Model.VoyageModel import Voyage

import csv

class VoyageData:
    def __init__(self):
        self.file_name = "src/Files/voyages.csv"
        
    def get_all_voyages(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile: 
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Voyage(row["vid"], row["departure_time"], row["arrival_time"], row["destination"], row["captain"], row["copilot"], row["fsm"], row["fa1"], row["fa2"], row["plane"]))
            return ret_list
        
    def create_voyage(self, voyage):
        pass