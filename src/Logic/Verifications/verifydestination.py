from Model.DestinationModel import Destination


class DestinationNameError(Exception):
    pass


class DestinationNameExistsError(Exception):
    pass


class DestinationCountryError(Exception):
    pass


class DestinationAirportError(Exception):
    pass


class DestinationAirportExistsError(Exception):
    pass


class DestinationDistanceError(Exception):
    pass


class DestinationFlightTimeError(Exception):
    pass


class DestinationContactError(Exception):
    pass


class DestinationContactNumberError(Exception):
    pass


class DestinationContactNumberExistsError(Exception):
    pass


class DestinationContactNumberLenghtError(Exception):
    pass


class VerifyDestination:
    def __init__(self, destination_info: Destination, data: list):
        self.data = data
        self.dest_to_validate = destination_info

        # self.name = destination_info.name
        # self.country = destination_info.country
        # self.airport = destination_info.airport
        # self.distance = destination_info.distance_from_Iceland
        # self.flight_time = destination_info.flight_time
        # self.contact_name = destination_info.contact_name
        # self.contact_phone_nr = destination_info.contact_phone_nr

    def Verify_Destination_Helper(self, info_type):
        in_use_info = []

        for i in range(len(self.data)):
            temp = self.data[i]
            in_use_info.append(getattr(temp, info_type))

        return in_use_info

    def Name(self):
        for character in self.dest_to_validate.name:
            if not (character == " " or character.isalpha()):
                raise DestinationNameError

        if self.dest_to_validate.name in self.Verify_Destination_Helper("name"):
            raise DestinationNameExistsError

        else:
            return True

    def Country(self):
        for character in self.dest_to_validate.country:
            if not (character == " " or character.isalpha()):
                raise DestinationCountryError

        else:
            return True

    def Airport(self):
        for character in self.dest_to_validate.airport:
            if not (character == " " or character.isalpha()):
                raise DestinationAirportError

        if self.dest_to_validate.airport in self.Verify_Destination_Helper("airport"):
            raise DestinationAirportExistsError

        else:
            return True

    def Distance(self):
        if not self.dest_to_validate.distance_from_Iceland.isdigit():
            raise DestinationDistanceError

        else:
            return True

    def Flight_time(self):
        if not self.dest_to_validate.flight_time.isdigit():
            raise DestinationFlightTimeError

        else:
            return True

    def Contact(self):
        for character in self.dest_to_validate.contact_name:
            if not (character == " " or character.isalpha()):
                raise DestinationContactError

        else:
            return True

    def Contact_number(self):
        temp = list(self.dest_to_validate.contact_phone_nr)

        if not temp[0] == "+":
            raise DestinationContactNumberError

        elif not self.dest_to_validate.contact_phone_nr.strip("+").isdigit():
            raise DestinationContactNumberError

        elif len(temp[1:]) != 10:
            raise DestinationContactNumberLenghtError

        elif self.dest_to_validate.contact_phone_nr in self.Verify_Destination_Helper(
            "contact_phone_nr"
        ):
            raise DestinationContactNumberExistsError

        else:
            return True

    def ValidateDestination(self):
        self.Name()
        self.Country()
        self.Airport()
        self.Distance()
        self.Flight_time()
        self.Distance()
        self.Contact()
        self.Contact_number()

    def ValidateDestinationUpdate(self, new_contact_name, new_contact_phonen_nr):
        self.dest_to_validate.contact_name = new_contact_name
        self.dest_to_validate.contact_phone_nr = new_contact_phonen_nr
        check = self.Contact() and self.Contact_number()
        return check
