from django.core.management.base import BaseCommand
from django.db import transaction

from lettings.models import Address, Letting
from oc_lettings_site.models import Address as LegacyAddress
from oc_lettings_site.models import Letting as LegacyLetting
from oc_lettings_site.models import Profile as LegacyProfile
from profiles.models import Profile


class Command(BaseCommand):
    help = (
        "Copy legacy data from oc_lettings_site tables "
        "into the new lettings and profiles tables."
    )

    @transaction.atomic
    def handle(self, *args, **options):

        # --- Copy Addresses ---
        created_addresses_count = 0

        for legacy_address in LegacyAddress.objects.all():
            _, created = Address.objects.update_or_create(
                id=legacy_address.id,
                defaults={
                    "number": legacy_address.number,
                    "street": legacy_address.street,
                    "city": legacy_address.city,
                    "state": legacy_address.state,
                    "zip_code": legacy_address.zip_code,
                    "country_iso_code": legacy_address.country_iso_code,
                },
            )
            if created:
                created_addresses_count += 1

        # --- Copy Lettings ---
        created_lettings_count = 0

        for legacy_letting in LegacyLetting.objects.all():
            _, created = Letting.objects.update_or_create(
                id=legacy_letting.id,
                defaults={
                    "title": legacy_letting.title,
                    "address_id": legacy_letting.address_id,
                },
            )
            if created:
                created_lettings_count += 1

        # --- Copy Profiles ---
        created_profiles_count = 0

        for legacy_profile in LegacyProfile.objects.all():
            _, created = Profile.objects.update_or_create(
                id=legacy_profile.id,
                defaults={
                    "user_id": legacy_profile.user_id,
                    "favorite_city": legacy_profile.favorite_city,
                },
            )
            if created:
                created_profiles_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                "Legacy data copied successfully.\n"
                f"- Addresses created: {created_addresses_count}\n"
                f"- Lettings created: {created_lettings_count}\n"
                f"- Profiles created: {created_profiles_count}"
            )
        )
