from dataclasses import asdict, replace, fields
from datetime import timedelta, datetime
from uuid import uuid4, UUID
import csv

from Model.VoyageModel import Voyage


class VoyageData:
    FILE_NAME = "src/Files/voyages.csv"

    def __init__(self, voyages: [Voyage] = []):
        self.voyages = voyages

    @classmethod
    def read_voyages_from_disk(cls, file_name=None):
        with open(file_name or cls.FILE_NAME, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            voyages = []
            for row in reader:
                row["departure"] = datetime.fromisoformat(row["departure"])
                row["arrival"] = datetime.fromisoformat(row["arrival"])
                voyages.append(Voyage(**row))
            return voyages

    @classmethod
    def write_voyages_to_disk(cls, voyages: [Voyage] = [], file_name=None):
        with open(file_name or cls.FILE_NAME, "w", newline="") as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=[f.name for f in fields(Voyage)]
            )
            writer.writeheader()
            for voyage in voyages:
                writer.writerow(asdict(voyage))

    def get_all_voyages(self):
        return self.voyages

    def register_new_voyage(self, voyage: Voyage):
        self.voyages.append(voyage)

    def find_voyage_by_id(self, voyage_id: UUID):
        for voyage in self.voyages:
            if voyage_id == voyage.id:
                return voyage
        return None

    def make_recurring_voyage(
        self, voyage_id: str, interval_in_days: int, end_date: datetime
    ):
        voyage = self.find_voyage_by_id(voyage_id)
        assert voyage, "Voyage ID needs to exist in table. Try again"
        difference = end_date - voyage.departure
        for i in range(0, difference.days + 1, interval_in_days):
            self.voyages.append(
                replace(
                    voyage,
                    departure=voyage.departure + timedelta(days=i),
                    arrival=voyage.arrival + timedelta(days=i),
                    id=uuid4(),
                )
            )

    def copy_to_new_date(self, voyage_id: str, new_date: datetime):
        voyage = self.find_voyage_by_id(voyage_id)
        assert voyage, "Voyage ID needs to exist in table. Try again"
        new_arrival = voyage.arrival + (
            new_date
            - voyage.departure.replace(
                minute=new_date.minute,
                hour=new_date.hour,
                second=new_date.second,
                microsecond=new_date.microsecond,
            )
        )
        new_departure = voyage.departure.replace(
            year=new_date.year, month=new_date.month, day=new_date.day
        )
        new_voyage = replace(
            voyage, arrival=new_arrival, departure=new_departure, id=uuid4()
        )
        self.voyages.append(new_voyage)

    def get_manned_voyages(self):
        manned_voyages = []
        for voyage in self.voyages:
            if (
                voyage.captain
                and voyage.copilot
                and voyage.flight_attendant
                and voyage.flight_service_manager
            ):
                manned_voyages.append(voyage)
        return manned_voyages

    def get_unmanned_voyages(self):
        unmanned_voyages = []
        for voyage in self.voyages:
            if (
                not voyage.captain
                or not voyage.copilot
                or not voyage.flight_attendant
                or not voyage.flight_service_manager
            ):
                unmanned_voyages.append(voyage)
        return unmanned_voyages

    def set_staff(self, voyage_id: str, **kwarg):
        for i, voyage in enumerate(self.voyages):
            if voyage_id == voyage.id:
                self.voyages[i] = replace(voyage, **kwarg)
