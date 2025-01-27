# Generated by Django 2.2.6 on 2019-10-07 17:28

from django.db import migrations
from django.utils.translation import gettext_lazy


def migrate_forward(apps, schema_editor):
    import dsmr_frontend.services
    import dsmr_backend.services.backend

    if dsmr_backend.services.backend.is_recent_installation():
        # Skip for new installations.
        return

    Notification = apps.get_model("dsmr_frontend", "Notification")
    Notification.objects.create(
        message=dsmr_frontend.services.get_translated_string(
            text=gettext_lazy(
                "DSMR-reader v2.6.0: Many changes related to MQTT. "
                "Messages are now sent using the RETAIN flag, telling the broker to cache the latest topic value received. "
                "This allows DSMR-reader to cache outgoing messages as well, preventing any duplicates sent.",
            )
        ),
        redirect_to="frontend:changelog-redirect",
    )


def migrate_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]

    dependencies = [
        ("dsmr_frontend", "0020_v230_release"),
    ]
