from dataclasses import dataclass
from Model.DestinationModel import Destination
from Model.EmployeeModel import Employee

@dataclass(frozen=False, order=True)
class Voyage:
    vid: str
    destination: Destination
    departuretime: str
    departuredate: str
    arrivaltime: str
    arrivaldate: str
    captain: Employee = "N/A"
    copilot: Employee = "N/A"
    flight_service_manager: Employee = "N/A"
    flight_attendant: Employee = "N/A"

