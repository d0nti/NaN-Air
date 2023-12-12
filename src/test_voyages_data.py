from Data.voyagesdata import VoyageData
from Model.VoyageModel import Voyage
from datetime import datetime
from dataclasses import fields


def unique_ids(objects):
    ids = [obj.id for obj in objects]
    return len(ids) == len(set(ids)), "IDs are not unique"


def test_get_all_voyages():
    voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name="test_data/voyages.csv")
    )
    all_voyages = voyages.get_all_voyages()
    assert len(all_voyages) == 10
    for i in range(len(all_voyages)):
        assert f"Destination {i}" in all_voyages[i].destination
    assert all_voyages[-1].flight_attendant == "FA 9"


def test_register_new_voyage():
    voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name="test_data/voyages.csv")
    )
    new_voyage = Voyage("KEF", "2020-11-11", "2020-11-12")
    voyages.register_new_voyage(new_voyage)
    assert len(voyages.get_all_voyages()) == 10 + 1


def test_find_voyage_by_id():
    voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name="test_data/voyages.csv")
    )
    assert (
        voyages.find_voyage_by_id("35d7ba70-3c2c-47de-90c8-0baf92b2dff8").destination
        == "Destination 1"
    )

def test_find_voyage_by_id_none():
    voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name="test_data/voyages.csv")
    )
    assert voyages.find_voyage_by_id("35d7ba70") is None


def test_make_recurring_voyage_daily():
    voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name="test_data/voyages.csv")
    )
    voyages.make_recurring_voyage(
        "35d7ba70-3c2c-47de-90c8-0baf92b2dff8", 1, datetime.fromisoformat("2023-06-30T22:07:46")
    )

    all_voyages = voyages.get_all_voyages()
    assert len(all_voyages) == 10 + 5
    assert unique_ids(all_voyages)


def test_make_recurring_voyage_daily_no_change():
    voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name="test_data/voyages.csv")
    )
    voyages.make_recurring_voyage(
        "35d7ba70-3c2c-47de-90c8-0baf92b2dff8", 1, datetime.fromisoformat("2023-06-26T22:07:46")
    )
    all_voyages = voyages.get_all_voyages()
    assert len(all_voyages) == 10 + 1
    assert unique_ids(all_voyages)


def test_make_recurring_voyage_every_three_days():
    voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name="test_data/voyages.csv")
    )
    voyages.make_recurring_voyage(
        "35d7ba70-3c2c-47de-90c8-0baf92b2dff8", 3, datetime.fromisoformat("2023-07-26T22:07:46")
    )
    all_voyages = voyages.get_all_voyages()
    assert len(all_voyages) == 10 + 11
    assert unique_ids(all_voyages)


def test_make_recurring_voyage_weekly():
    voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name="test_data/voyages.csv")
    )
    voyages.make_recurring_voyage(
        "13e7f26f-e8d4-48fe-a7d7-e22dd9b3a6a6", 7, datetime.fromisoformat("2024-05-10T00:32:31")
    )
    all_voyages = voyages.get_all_voyages()
    assert len(all_voyages) == 10 + 53
    assert unique_ids(all_voyages)


def test_make_recurring_voyage_biweekly():
    voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name="test_data/voyages.csv")
    )
    voyages.make_recurring_voyage(
        "13e7f26f-e8d4-48fe-a7d7-e22dd9b3a6a6", 14, datetime.fromisoformat("2024-05-10T00:32:31")
    )
    all_voyages = voyages.get_all_voyages()
    assert len(all_voyages) == 10 + 27
    assert unique_ids(all_voyages)


def test_make_recurring_voyage_every_thirty_days():
    voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name="test_data/voyages.csv")
    )
    voyages.make_recurring_voyage(
        "02203cd1-7c6f-4be2-b98f-63e9ed48ea43", 30, datetime.fromisoformat("2025-08-23T22:09:04")
    )
    all_voyages = voyages.get_all_voyages()
    assert len(all_voyages) == 11 + 24
    assert unique_ids(all_voyages)


def test_copy_to_new_date():
    voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name="test_data/voyages.csv")
    )

    original_departure = datetime.fromisoformat("2023-08-23T22:09:04")
    expected_departure = original_departure.replace(day=24)

    original_arrival = datetime.fromisoformat("2023-08-24T09:09:04")
    expected_arrival = original_arrival.replace(day=25)

    new_date = datetime(2023, 8, 24)

    voyages.copy_to_new_date("02203cd1-7c6f-4be2-b98f-63e9ed48ea43", new_date)

    all_voyages = voyages.get_all_voyages()
    assert len(all_voyages) == 10 + 1
    assert unique_ids(all_voyages)
    assert all_voyages[-1].departure == expected_departure
    assert all_voyages[-1].arrival == expected_arrival


def test_read_write_to_disk():
    file_name="test_data/voyages.csv"
    voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name)
    )

    VoyageData.write_voyages_to_disk(voyages.get_all_voyages(), file_name)

    new_voyages = VoyageData(
        VoyageData.read_voyages_from_disk(file_name)
    )

    assert voyages.get_all_voyages() == new_voyages.get_all_voyages()
