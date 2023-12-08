from Model.VoyageModel import Voyage


class VoyagesLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        
    def register_voyage(self, voyage_info):
        self.data_wrapper.register_new_voyage(voyage_info)
        
    def get_single_voyage_given_vid(self, vid):
        for voyage in Voyage.voyages:
            if voyage.vid == vid:
                return voyage
        return None
        
    def get_all_voyages(self):
        return self.data_wrapper.get_all_voyages()
    
    def search_voyages(self, filter):
        voyages = self.data_wrapper.get_all_voyages(filter)
        pass
    
    def copy_voyage(self, voyage_info):
        pass
    
    def make_recurring_voyage(self, voyage_info):
        pass
    
    def edit_voyage(self, voyage_info):
        pass
    
    def staff_voyage(self, voyage_info):
        pass
    
    def add_cap_to_voyage(self, voyage_info):
        pass
    
    def add_copilot_to_voyage(self, voyage_info):
        pass
    
    def add_flight_attendant_to_voyage(self, voyage_info):
        pass
    
    def add_head_of_service_to_voyage(self, voyage_info):
        pass
    
    