
class AirplaneLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def register_airplane(self):
        pass

    def get_all_airplanes(self):
        return self.data_wrapper.get_all_airplanes()

