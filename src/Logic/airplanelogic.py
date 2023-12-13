from Logic.Verifications.verifyairplane import VerifyAirplane


class AirplaneLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def get_all_airplanes(self):
        return self.data_wrapper.get_all_airplanes()

    def register_airplane(self, airplane_info):
        temp = VerifyAirplane(airplane_info, self.get_all_airplanes())
        temp.validate_plane()
        if temp:
            self.data_wrapper.register_airplane(airplane_info)

    def search_airplane(self, filter):
        return self.data_wrapper.search_airplane(filter)
