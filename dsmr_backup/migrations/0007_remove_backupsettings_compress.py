# Generated by Django 2.2.4 on 2019-08-15 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dsmr_backup", "0006_scheduled_email_backup"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="backupsettings",
            name="compress",
        ),
    ]
