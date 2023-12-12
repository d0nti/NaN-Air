from Model.VoyageModel import Voyage
from datetime import datetime


class VoyagesLogic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def register_new_voyage(self, voyage_info):
        self.data_wrapper.register_new_voyage(voyage_info)

    def get_single_voyage_given_uuid(self, uuid):
        for voyage in Voyage.voyages:
            if voyage.uuid == uuid:
                return voyage
        return None

    def get_all_voyages(self):
        return self.data_wrapper.get_all_voyages()

    def find_voyage(self, voyage_id: str):
        return self.data_wrapper.find_voyage(voyage_id)

    def copy_to_new_date(self, voyage_id: str, new_date: datetime):
        return self.data_wrapper.copy_to_new_date(voyage_id, new_date)

    def make_recurring_voyage(
        self, voyage_id: str, interval_in_days: int, end_date: datetime
    ):
        return self.data_wrapper.make_recurring_voyage(
            voyage_id, interval_in_days, end_date
        )

    def get_manned_voyages(self):
        return self.data_wrapper.get_manned_voyages()

    def get_unmanned_voyages(self):
        return self.data_wrapper.get_unmanned_voyages()

    def edit_voyage(self, voyage_info):
        pass

    def populate_voyage(self, voyage_info):
        pass

    def add_captain_to_voyage(self, voyage_info):
        pass

    def add_copilot_to_voyage(self, voyage_info):
        pass

    def add_flight_attendant_to_voyage(self, voyage_info):
        pass

    def add_head_of_service_to_voyage(self, voyage_info):
        pass
