from dataclasses import dataclass, field
import uuid
from Model.DestinationModel import Destination
from Model.EmployeeModel import Employee
from datetime import datetime


@dataclass(frozen=False, order=True)
class Voyage:
    destination: Destination
    departure: datetime
    arrival: datetime
    captain: Employee = None
    copilot: Employee = None
    flight_service_manager: Employee = None
    flight_attendant: Employee = None
    id: uuid.UUID = field(default_factory=uuid.uuid4)