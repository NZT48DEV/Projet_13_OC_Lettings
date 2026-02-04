import pytest
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.utils import IntegrityError

from lettings.models import Address, Letting


def test_address_create_fails_when_street_is_none(db, address_data_dict):
    copy_data = address_data_dict.copy()
    copy_data["street"] = None
    obj = Address(**copy_data)
    with pytest.raises(ValidationError) as exc_info:
        obj.full_clean()
    errors = exc_info.value.message_dict
    assert "street" in errors


def test_letting_can_be_created(address: Address, letting: Letting):
    assert letting.pk is not None
    assert letting.address == address


def test_letting_cannot_share_same_address(letting: Letting):
    address = letting.address
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Letting.objects.create(
                title="Title Test",
                address=address,
            )


def test_deleting_address_deletes_letting(letting: Letting):
    address = letting.address
    address.delete()
    assert not Address.objects.filter(pk=address.pk).exists()
    assert not Letting.objects.filter(pk=letting.pk).exists()


def test_deleting_letting_not_deletes_address(letting: Letting):
    address = letting.address
    address_pk = address.pk
    letting_pk = letting.pk
    letting.delete()
    assert Address.objects.filter(pk=address_pk).exists()
    assert not Letting.objects.filter(pk=letting_pk).exists()
