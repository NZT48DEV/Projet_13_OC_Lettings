import pytest

from lettings.models import Address, Letting


@pytest.fixture
def address_data_dict():
    return {
        "number": 7217,
        "street": "Military Street",
        "city": "Brunswick",
        "state": "GA",
        "zip_code": 31525,
        "country_iso_code": "USA",
    }


@pytest.fixture
def address(db, address_data_dict):
    address_obj = Address.objects.create(**address_data_dict)
    return address_obj


@pytest.fixture
def letting(db, address):
    letting_obj = Letting.objects.create(title="Test Titre", address=address)
    return letting_obj
