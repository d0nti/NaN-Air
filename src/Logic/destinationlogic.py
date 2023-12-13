from Logic.Verifications.verifydestination import VerifyDestination
from Model.DestinationModel import Destination


class DestinationLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_destination(self, destination_info):
        verifier = VerifyDestination(destination_info, self.get_all_destinations())
        verifier.ValidateDestination()
        if verifier:
            self.data_wrapper.register_destination(destination_info)

    def get_all_destinations(self):
        return self.data_wrapper.get_all_destinations()

    def search_destination(self, filter):
        return self.data_wrapper.search_destination(filter)

    def update_destination(
        self, destination: Destination, contact_name, contact_phone_nr
    ):
        all_destinations = self.get_all_destinations()
        verifier = VerifyDestination(destination, all_destinations)

        if verifier.ValidateDestinationUpdate(contact_name, contact_phone_nr):
            destination.contact_name = contact_name
            destination.contact_phone_nr = contact_phone_nr
            self.data_wrapper.update_destination(destination)
