# Generated by Django 3.1.7 on 2021-03-08 20:00

from django.db import migrations
from django.conf import settings


def migrate_forward(apps, schema_editor):
    ScheduledProcess = apps.get_model("dsmr_backend", "ScheduledProcess")
    DropboxSettings = apps.get_model("dsmr_backup", "DropboxSettings")

    dropbox_settings, _ = DropboxSettings.objects.get_or_create()
    ScheduledProcess.objects.create(
        name="Dropbox export",
        module=settings.DSMRREADER_MODULE_DROPBOX_EXPORT,
        active=bool(dropbox_settings.refresh_token),
    )


def migrate_backward(apps, schema_editor):
    ScheduledProcess = apps.get_model("dsmr_backend", "ScheduledProcess")
    ScheduledProcess.objects.filter(
        module=settings.DSMRREADER_MODULE_DROPBOX_EXPORT
    ).delete()


class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]

    dependencies = []
