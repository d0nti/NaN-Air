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
    captain: str = None
    copilot: str = None
    flight_service_manager: str = None
    flight_attendant: str = None
    id: uuid.UUID = field(default_factory=uuid.uuid4)
