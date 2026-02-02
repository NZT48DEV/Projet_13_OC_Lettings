import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

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

data_dict = {
    "number": 5000,
    "street": "rue des fleurs",
    "city": "Strasbourg",
    "state": "LA",
    "zip_code": 75985,
    "country_iso_code": "USA",
}


@pytest.mark.parametrize("field,value", VALID_CASES)
def test_validators_valid(field, value):
    copy_data = data_dict.copy()
    copy_data[field] = value
    obj = Address(**copy_data)
    obj.full_clean()


@pytest.mark.parametrize("field,value", INVALID_CASES)
def test_validators_invalid(field, value):
    copy_data = data_dict.copy()
    copy_data[field] = value
    obj = Address(**copy_data)
    with pytest.raises(ValidationError) as exc_info:
        obj.full_clean()
    errors = exc_info.value.message_dict
    assert field in errors


@pytest.mark.django_db
def test_address_is_valid():
    address_data = Address.objects.create(**data_dict)
    assert 5000 == address_data.number
    assert "rue des fleurs" == address_data.street
    assert "Strasbourg" == address_data.city
    assert "LA" == address_data.state
    assert 75985 == address_data.zip_code
    assert "USA" == address_data.country_iso_code


@pytest.mark.django_db
def test_address_create_fails_when_street_is_none():
    copy_data = data_dict.copy()
    copy_data["street"] = None
    with pytest.raises(IntegrityError):
        Address.objects.create(**copy_data)


@pytest.mark.django_db
def test_address_str():
    address_data = Address.objects.create(**data_dict)
    str_address_data = str(address_data)
    assert "5000 rue des fleurs" == str_address_data
