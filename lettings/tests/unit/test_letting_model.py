import pytest
from django.db import transaction
from django.db.utils import IntegrityError

from lettings.models import Address, Letting

address_data_dict = {
    "number": 5000,
    "street": "rue des fleurs",
    "city": "Strasbourg",
    "state": "LA",
    "zip_code": 75985,
    "country_iso_code": "USA",
}


@pytest.mark.django_db
def test_letting_can_be_created():
    address = Address.objects.create(**address_data_dict)
    letting = Letting.objects.create(
        title="Test Titre",
        address=address,
    )
    assert letting.pk is not None
    assert letting.address == address


@pytest.mark.django_db
def test_str_letting():
    address = Address.objects.create(**address_data_dict)
    letting = Letting.objects.create(
        title="Test Titre",
        address=address,
    )
    result = str(letting)
    assert result == letting.title


@pytest.mark.django_db
def test_letting_cannot_share_same_address():
    address = Address.objects.create(**address_data_dict)
    Letting.objects.create(
        title="Test Titre",
        address=address,
    )
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Letting.objects.create(
                title="Test Titre",
                address=address,
            )


@pytest.mark.django_db
def test_deleting_address_deletes_letting():
    address = Address.objects.create(**address_data_dict)
    letting = Letting.objects.create(
        title="Test Titre",
        address=address,
    )
    address.delete()
    assert not Address.objects.filter(pk=address.pk).exists()
    assert not Letting.objects.filter(pk=letting.pk).exists()


@pytest.mark.django_db
def test_deleting_letting_not_deletes_address():
    address = Address.objects.create(**address_data_dict)
    letting = Letting.objects.create(
        title="Test Titre",
        address=address,
    )
    letting.delete()
    assert Address.objects.filter(pk=address.pk).exists()
    assert not Letting.objects.filter(pk=letting.pk).exists()
