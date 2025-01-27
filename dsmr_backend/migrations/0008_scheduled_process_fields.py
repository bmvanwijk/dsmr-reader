# Generated by Django 2.2.6 on 2019-11-06 19:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("dsmr_backend", "0007_schedule_stats_generator"),
    ]

    operations = [
        migrations.AddField(
            model_name="scheduledprocess",
            name="last_executed_at",
            field=models.DateTimeField(
                default=None,
                help_text="The last moment this process ran (disregarding whether it succeeded or failed).",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="scheduledprocess",
            name="active",
            field=models.BooleanField(
                db_index=True,
                default=True,
                help_text="Related configuration settings manage whether this process is active or disabled for you.",
            ),
        ),
        migrations.AlterField(
            model_name="scheduledprocess",
            name="planned",
            field=models.DateTimeField(
                db_index=True,
                default=django.utils.timezone.now,
                help_text="The next moment this process will run again.",
            ),
        ),
    ]
