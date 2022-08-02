# Generated by Django 3.0.3 on 2020-02-18 20:45

from django.db import migrations
from django.utils.translation import ugettext_lazy


def migrate_forward(apps, schema_editor):
    import dsmr_frontend.services
    import dsmr_backend.services.backend

    if dsmr_backend.services.backend.is_recent_installation():
        # Skip for new installations.
        return

    Notification = apps.get_model("dsmr_frontend", "Notification")
    Notification.objects.create(
        message=dsmr_frontend.services.get_translated_string(
            text=ugettext_lazy(
                "DSMR-reader v3.4.0 (1/3): Archive graphs are now in bar style + stacked by default. You can change or "
                "revert this using the admin interface in the Frontend configuration."
            )
        ),
        redirect_to="frontend:changelog-redirect",
    )
    Notification.objects.create(
        message=dsmr_frontend.services.get_translated_string(
            text=ugettext_lazy(
                "DSMR-reader v3.4.0 (2/3): Starting this release you can (re)name the electricity tariffs yourself. Visit "
                "the admin interface in the Frontend configuration to use your own names."
            )
        ),
        redirect_to="frontend:changelog-redirect",
    )
    Notification.objects.create(
        message=dsmr_frontend.services.get_translated_string(
            text=ugettext_lazy(
                'DSMR-reader v3.4.0 (3/3): Graphs formerly displayed on the Dashboard are now available in "Live graphs".'
            )
        ),
        redirect_to="frontend:live-graphs",
    )


def migrate_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]

    dependencies = [
        ("dsmr_frontend", "0031_tariff_names"),
    ]
