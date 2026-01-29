from django.db import migrations

def copy_legacy_lettings(apps, schema_editor):
    LegacyAddress = apps.get_model("oc_lettings_site", "Address")
    LegacyLetting = apps.get_model("oc_lettings_site", "Letting")

    Address = apps.get_model("lettings", "Address")
    Letting = apps.get_model("lettings", "Letting")

    # évite de dupliquer si tu relances la migration
    if Address.objects.exists() or Letting.objects.exists():
        return

    addresses = [
        Address(
            id=a.id,
            number=a.number,
            street=a.street,
            city=a.city,
            state=a.state,
            zip_code=a.zip_code,
            country_iso_code=a.country_iso_code,
        )
        for a in LegacyAddress.objects.all()
    ]
    Address.objects.bulk_create(addresses)

    lettings = [
        Letting(
            id=l.id,
            title=l.title,
            address_id=l.address_id,  # conserve la relation 1-1
        )
        for l in LegacyLetting.objects.all()
    ]
    Letting.objects.bulk_create(lettings)

class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(copy_legacy_lettings, migrations.RunPython.noop),
    ]
