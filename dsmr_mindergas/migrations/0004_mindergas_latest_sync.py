# Generated by Django 2.0.7 on 2018-07-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dsmr_mindergas", "0003_mindergas_next_export_datetime"),
    ]

    operations = [
        migrations.AddField(
            model_name="mindergassettings",
            name="latest_sync",
            field=models.DateTimeField(
                blank=True,
                default=None,
                help_text="Timestamp of latest sync with MinderGas. Automatically updated by application.",
                null=True,
                verbose_name="Latest sync",
            ),
        ),
    ]
