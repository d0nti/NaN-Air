class DestinationLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_destination(self, destination):
        self.data_wrapper.create_destination(destination)


    def get_all_destinations(self):
        return self.data_wrapper.get_all_destinations()

    def search(self, filter):
        return self.data_wrapper.search(filter)
