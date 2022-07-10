# Generated by Django 3.2.14 on 2022-07-10 18:38

from django.db import migrations, models


# Rename tariffs, but only when still using the previous defaults, as we don't want to override personal preferences
MAP = {
    'tariff_1_delivered_name': ('Laagtarief', 'Daltarief'),
    'tariff_2_delivered_name': ('Hoogtarief', 'Normaaltarief'),
    'tariff_1_returned_name': ('Laagtarief teruglevering', 'Daltarief teruglevering'),
    'tariff_2_returned_name': ('Hoogtarief teruglevering', 'Normaaltarief teruglevering'),
}


def migrate_forward(apps, schema_editor):
    FrontendSettings = apps.get_model('dsmr_frontend', 'FrontendSettings')

    for field, find_replace in MAP.items():
        old_name, new_name = find_replace

        FrontendSettings.objects.filter(
            **{field: old_name}
        ).update(
            **{field: new_name}
        )


def migrate_backward(apps, schema_editor):
    FrontendSettings = apps.get_model('dsmr_frontend', 'FrontendSettings')

    for field, find_replace in MAP.items():
        new_name, old_name = find_replace  # Swapped, compared to migrate_forward()

        FrontendSettings.objects.filter(
            **{field: old_name}
        ).update(
            **{field: new_name}
        )

class Migration(migrations.Migration):
    operations = [
        migrations.AlterField(
            model_name='frontendsettings',
            name='tariff_1_delivered_name',
            field=models.CharField(default='Daltarief', help_text="Dutch users: Defaults to 'low tariff' delivered", max_length=30, verbose_name='Name of tariff 1 (delivered)'),
        ),
        migrations.AlterField(
            model_name='frontendsettings',
            name='tariff_1_returned_name',
            field=models.CharField(default='Daltarief teruglevering', help_text="Dutch users: Defaults to 'low tariff' returned", max_length=30, verbose_name='Name of tariff 1 (returned)'),
        ),
        migrations.AlterField(
            model_name='frontendsettings',
            name='tariff_2_delivered_name',
            field=models.CharField(default='Normaaltarief', help_text="Dutch users: Defaults to 'normal tariff' delivered", max_length=30, verbose_name='Name of tariff 2 (delivered)'),
        ),
        migrations.AlterField(
            model_name='frontendsettings',
            name='tariff_2_returned_name',
            field=models.CharField(default='Normaaltarief teruglevering', help_text="Dutch users: Defaults to 'normal tariff' returned", max_length=30, verbose_name='Name of tariff 2 (returned)'),
        ),
        migrations.RunPython(migrate_forward, migrate_backward),
    ]

    dependencies = [
        ('dsmr_frontend', '0046_gui_refresh_interval'),
    ]
