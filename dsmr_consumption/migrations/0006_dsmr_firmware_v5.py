# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dsmr_consumption", "0005_phase_currently_delivered"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="electricityconsumption",
            options={
                "default_permissions": (),
                "verbose_name": "Electricity consumption",
            },
        ),
        migrations.AlterModelOptions(
            name="gasconsumption",
            options={"default_permissions": (), "verbose_name": "Gas consumption"},
        ),
        migrations.AlterField(
            model_name="gasconsumption",
            name="currently_delivered",
            field=models.DecimalField(
                decimal_places=3,
                help_text="Delivered value, based on the previous reading",
                max_digits=9,
            ),
        ),
        migrations.AlterField(
            model_name="gasconsumption",
            name="delivered",
            field=models.DecimalField(
                decimal_places=3, help_text="Last meter position read", max_digits=9
            ),
        ),
    ]
