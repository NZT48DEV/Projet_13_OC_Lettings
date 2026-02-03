import pytest
from django.core.exceptions import ValidationError

from lettings.models import Address

VALID_CASES = [
    ("number", 9_999),
    ("state", "NY"),
    ("zip_code", 99_999),
    ("country_iso_code", "USA"),
]

INVALID_CASES = [
    ("number", 10_000),
    ("state", "L"),
    ("zip_code", 100_000),
    ("country_iso_code", "US"),
]


@pytest.mark.parametrize("field,value", VALID_CASES)
def test_validators_valid(field, value, address_data_dict):
    copy_data = address_data_dict.copy()
    copy_data[field] = value
    obj = Address(**copy_data)
    obj.full_clean()


@pytest.mark.parametrize("field,value", INVALID_CASES)
def test_validators_invalid(field, value, address_data_dict):
    copy_data = address_data_dict.copy()
    copy_data[field] = value
    obj = Address(**copy_data)
    with pytest.raises(ValidationError) as exc_info:
        obj.full_clean()
    errors = exc_info.value.message_dict
    assert field in errors


def test_address_is_valid(address: Address):
    assert 5000 == address.number
    assert "rue des fleurs" == address.street
    assert "Strasbourg" == address.city
    assert "LA" == address.state
    assert 75985 == address.zip_code
    assert "USA" == address.country_iso_code


def test_address_create_fails_when_street_is_none(db, address_data_dict):
    copy_data = address_data_dict.copy()
    copy_data["street"] = None
    obj = Address(**copy_data)
    with pytest.raises(ValidationError) as exc_info:
        obj.full_clean()
    errors = exc_info.value.message_dict
    assert "street" in errors


def test_address_str(address):
    str_address = str(address)
    assert "5000 rue des fleurs" == str_address
