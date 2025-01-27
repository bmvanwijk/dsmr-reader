# Generated by Django 3.0.2 on 2020-01-14 17:18

from django.db import migrations


def migrate_forward(apps, schema_editor):
    # Delete this notification, as the target URL no longer exists in v3.
    Notification = apps.get_model("dsmr_frontend", "Notification")
    Notification.objects.filter(redirect_to="frontend:v3-upgrade-redirect").delete()


def migrate_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]

    dependencies = [
        ("dsmr_frontend", "0027_v215_release"),
    ]
