from Logic.Verifications.verifydestination import VerifyDestination
from Model.DestinationModel import Destination

class DestinationSearchFilterNotFoundError(Exception):
    pass


class DestinationLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_destination(self, destination_info: Destination):
        verifier = VerifyDestination(destination_info, self.get_all_destinations())
        verifier.ValidateDestination()
        if verifier:
            self.data_wrapper.register_destination(destination_info)

    def get_all_destinations(self):
        return self.data_wrapper.get_all_destinations()

    def search_destination(self, filter: str):
        all_destinations = self.get_all_destinations()
        found_destination = None
        for destination in all_destinations:
            if (
                destination.name == filter
                or destination.country == filter
                or destination.airport == filter
                or destination.flight_time == filter
                or destination.distance_from_Iceland == filter
                or destination.contact_name == filter
                or destination.contact_phone_nr == filter
            ):
                found_destination = destination
        if found_destination != None:
            return self.data_wrapper.search_destination(filter)
        else:
            raise DestinationSearchFilterNotFoundError

    def update_destination(self, destination: Destination, contact_name: str, contact_phone_nr: str):
        all_destinations = self.get_all_destinations()
        verifier = VerifyDestination(destination, all_destinations)

        if verifier.ValidateDestinationUpdate(contact_name, contact_phone_nr):
            destination.contact_name = contact_name
            destination.contact_phone_nr = contact_phone_nr
            self.data_wrapper.update_destination(destination)
