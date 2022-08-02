# Generated by Django 3.1 on 2020-08-24 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dsmr_consumption", "0015_track_power_current"),
    ]

    operations = [
        migrations.AddField(
            model_name="energysupplierprice",
            name="fixed_daily_cost",
            field=models.DecimalField(
                decimal_places=5,
                default=0,
                help_text="A fixed price added to the totals of each day",
                max_digits=11,
                verbose_name="Fixed daily costs",
            ),
        ),
    ]
