# Generated by Django 2.0.7 on 2018-07-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dsmr_datalogger", "0009_retention_settings"),
    ]

    operations = [
        migrations.AddField(
            model_name="dsmrreading",
            name="phase_currently_returned_l1",
            field=models.DecimalField(
                decimal_places=3,
                default=None,
                help_text="Current electricity returned by phase L1 (in kW)",
                max_digits=9,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="dsmrreading",
            name="phase_currently_returned_l2",
            field=models.DecimalField(
                decimal_places=3,
                default=None,
                help_text="Current electricity returned by phase L2 (in kW)",
                max_digits=9,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="dsmrreading",
            name="phase_currently_returned_l3",
            field=models.DecimalField(
                decimal_places=3,
                default=None,
                help_text="Current electricity returned by phase L3 (in kW)",
                max_digits=9,
                null=True,
            ),
        ),
    ]
