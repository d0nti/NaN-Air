from Logic.Verifications.verifydestination import VerifyDestination


class DestinationLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_destination(self, destination_info):
        temp = VerifyDestination(destination_info)
        temp.ValidateDestination()
        if temp:
            self.data_wrapper.register_destination(destination_info)

    def get_all_destinations(self):
        return self.data_wrapper.get_all_destinations()

    def search_destination(self, filter):
        return self.data_wrapper.search(filter)
