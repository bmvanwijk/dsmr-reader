# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-18 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dsmr_stats", "0009_statistics_editable"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="daystatistics",
            options={
                "default_permissions": (),
                "ordering": ["day"],
                "verbose_name": "Day statistics (automatically generated data)",
                "verbose_name_plural": "Day statistics (automatically generated data)",
            },
        ),
        migrations.AlterModelOptions(
            name="hourstatistics",
            options={
                "default_permissions": (),
                "ordering": ["hour_start"],
                "verbose_name": "Hour statistics (automatically generated data)",
                "verbose_name_plural": "Hour statistics (automatically generated data)",
            },
        ),
        migrations.AlterField(
            model_name="daystatistics",
            name="day",
            field=models.DateField(db_index=True, unique=True, verbose_name="Date"),
        ),
        migrations.AlterField(
            model_name="hourstatistics",
            name="hour_start",
            field=models.DateTimeField(
                db_index=True, unique=True, verbose_name="Hour start"
            ),
        ),
    ]
