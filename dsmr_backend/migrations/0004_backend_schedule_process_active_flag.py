# Generated by Django 2.2.6 on 2019-11-04 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dsmr_backend', '0003_scheduled_processes'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledprocess',
            name='active',
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name='scheduledprocess',
            name='planned',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
