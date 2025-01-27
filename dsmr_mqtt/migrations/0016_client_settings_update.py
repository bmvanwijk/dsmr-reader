# Generated by Django 3.0.8 on 2020-07-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dsmr_mqtt", "0015_continuous_client"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="message",
            options={
                "default_permissions": ("delete",),
                "verbose_name": "Outgoing MQTT message",
                "verbose_name_plural": "Outgoing MQTT messages",
            },
        ),
        migrations.AlterField(
            model_name="mqttbrokersettings",
            name="hostname",
            field=models.CharField(
                blank=True,
                default="localhost",
                help_text="The hostname of the broker to send MQTT messages to.",
                max_length=256,
                verbose_name="Hostname",
            ),
        ),
    ]
