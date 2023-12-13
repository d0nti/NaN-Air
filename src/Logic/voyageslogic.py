from Model.VoyageModel import Voyage
from datetime import datetime


class VoyagesLogic:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def register_new_voyage(self, voyage_info):
        self.data_wrapper.register_new_voyage(voyage_info)

    def write_voyages_to_disk(self):
        self.data_wrapper.write_voyages_to_disk()

    def get_single_voyage_given_uuid(self, uuid):
        return self.data_wrapper.find_voyage_by_id(uuid)

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

    def set_staff(self, voyage_id: str, **kwarg):
        return self.data_wrapper.set_staff(voyage_id, **kwarg)
