# Generated by Django 3.0.3 on 2020-02-20 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dsmr_stats", "0013_all_time_low"),
    ]

    operations = [
        migrations.AlterField(
            model_name="daystatistics",
            name="total_cost",
            field=models.DecimalField(
                db_index=True, decimal_places=2, max_digits=8, verbose_name="Total cost"
            ),
        ),
    ]
