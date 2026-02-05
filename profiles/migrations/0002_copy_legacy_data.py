from django.db import migrations


def copy_legacy_profiles(apps, schema_editor):
    LegacyProfile = apps.get_model("oc_lettings_site", "Profile")
    Profile = apps.get_model("profiles", "Profile")

    if Profile.objects.exists():
        return

    profiles = [
        Profile(
            id=p.id,
            favorite_city=p.favorite_city,
            user_id=p.user_id,
        )
        for p in LegacyProfile.objects.all()
    ]
    Profile.objects.bulk_create(profiles)


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(copy_legacy_profiles, migrations.RunPython.noop),
    ]
