# Generated by Django 2.0.9 on 2019-04-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dsmr_datalogger", "0010_phases_currently_returned"),
    ]

    operations = [
        migrations.AddField(
            model_name="meterstatistics",
            name="latest_telegram",
            field=models.TextField(
                default=None,
                help_text="The latest telegram succesfully read. Please note that only the latest telegram is saved here and will be overwritten each time.",
                null=True,
            ),
        ),
    ]
