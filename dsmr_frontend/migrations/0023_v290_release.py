# Generated by Django 2.2.6 on 2019-10-25 16:02


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
                "DSMR-reader v2.9.0: Buienradar changed their API. This update fixes the issue.",
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
        ("dsmr_frontend", "0022_v270_release"),
    ]
