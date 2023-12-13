class DestinationNameError(Exception):
    pass


class DestinationNameExistsError(Exception):
    pass


class DestinationCountryError(Exception):
    pass


class DestinationCountryExistsError(Exception):
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


class DestinationContactExistsError(Exception):
    pass


class DestinationContactNumberError(Exception):
    pass


class DestinationContactNumberExistsError(Exception):
    pass


class DestinationContactNumberLenghtError(Exception):
    pass


class VerifyDestination:
    def __init__(self, destination_info: object, data: list) -> None:
        self.data = data
        self.name = destination_info.name
        self.country = destination_info.country
        self.airport = destination_info.airport
        self.distance = destination_info.distance_from_Iceland
        self.flight_time = destination_info.flight_time
        self.contact_name = destination_info.contact_name
        self.contact_phone_nr = destination_info.contact_phone_nr

    def Verify_Destination_Helper(self, info_type):
        in_use_info = []

        for i in range(len(self.data)):
            temp = self.data[i]
            in_use_info.append(getattr(temp, info_type))

        return in_use_info

    def Name(self):
        if self.name.isdigit():
            raise DestinationNameError

        elif self.name in self.Verify_Destination_Helper("name"):
            raise DestinationNameExistsError

        else:
            return True

    def Country(self):
        if self.country.isdigit():
            raise DestinationCountryError

        else:
            return True

    def Airport(self):
        if self.airport.isdigit():
            raise DestinationAirportError

        elif self.airport in self.Verify_Destination_Helper("airport"):
            raise DestinationAirportExistsError

        else:
            return True

    def Distance(self):
        if not self.distance.lower().strip("km. ").isdigit():
            raise DestinationDistanceError

        else:
            return True

    def Flight_time(self):
        if not self.flight_time.isdigit():
            raise DestinationFlightTimeError

        else:
            return True

    def Contact(self):
        if self.contact_name.isdigit():
            raise DestinationContactError

        elif self.contact_name in self.Verify_Destination_Helper("contact_name"):
            raise DestinationContactExistsError

        else:
            return True

    def Contact_number(self):
        temp = list(self.contact_phone_nr)
        print(temp[1:])

        if not temp[0] == "+":
            raise DestinationContactNumberError

        elif not self.contact_phone_nr.strip("+").isdigit():
            raise DestinationContactNumberError

        elif len(temp[1:]) != 10:
            raise DestinationContactNumberLenghtError

        elif self.contact_phone_nr in self.Verify_Destination_Helper(
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
