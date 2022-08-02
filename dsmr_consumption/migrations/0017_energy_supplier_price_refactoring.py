# Generated by Django 3.1.1 on 2020-09-08 20:33

from dateutil import relativedelta
import django.core.validators
from django.db import migrations, models


def migrate_forward(apps, schema_editor):
    import dsmr_backend.services.backend

    if dsmr_backend.services.backend.is_recent_installation():
        # Skip for new installations.
        return

    EnergySupplierPrice = apps.get_model("dsmr_consumption", "EnergySupplierPrice")

    for current in EnergySupplierPrice.objects.filter(end__isnull=True):
        current.end = current.start + relativedelta.relativedelta(years=10)
        current.save()

    # Fix NULL's
    EnergySupplierPrice.objects.filter(description__isnull=True).update(description="")


def migrate_backward(apps, schema_editor):
    # Unable to revert.
    pass


class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
        migrations.AlterModelOptions(
            name="energysupplierprice",
            options={
                "default_permissions": (),
                "verbose_name": "Energy supplier (price) contract",
                "verbose_name_plural": "Energy supplier (price) contracts",
            },
        ),
        migrations.AlterField(
            model_name="energysupplierprice",
            name="description",
            field=models.CharField(
                help_text="For your own reference, i.e. the name of your supplier",
                max_length=255,
                verbose_name="Contract name",
            ),
        ),
        migrations.AlterField(
            model_name="energysupplierprice",
            name="electricity_delivered_1_price",
            field=models.DecimalField(
                decimal_places=5,
                default=0,
                help_text="Set to zero when: Unused / Defined in other contract / Not applicable to your situation",
                max_digits=11,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Tariff 1 delivered price (€)",
            ),
        ),
        migrations.AlterField(
            model_name="energysupplierprice",
            name="electricity_delivered_2_price",
            field=models.DecimalField(
                decimal_places=5,
                default=0,
                help_text="Set to zero when: Unused / Defined in other contract / Not applicable to your situation",
                max_digits=11,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Tariff 2 delivered price (€)",
            ),
        ),
        migrations.AlterField(
            model_name="energysupplierprice",
            name="electricity_returned_1_price",
            field=models.DecimalField(
                decimal_places=5,
                default=0,
                help_text="Set to zero when: Unused / Defined in other contract / Not applicable to your situation",
                max_digits=11,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Tariff 1 returned price (€)",
            ),
        ),
        migrations.AlterField(
            model_name="energysupplierprice",
            name="electricity_returned_2_price",
            field=models.DecimalField(
                decimal_places=5,
                default=0,
                help_text="Set to zero when: Unused / Defined in other contract / Not applicable to your situation",
                max_digits=11,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Tariff 2 returned price (€)",
            ),
        ),
        migrations.AlterField(
            model_name="energysupplierprice",
            name="end",
            field=models.DateField(
                db_index=True,
                help_text="Set to a far future date when there is not contract end.",
                verbose_name="Contract end",
            ),
        ),
        migrations.AlterField(
            model_name="energysupplierprice",
            name="fixed_daily_cost",
            field=models.DecimalField(
                decimal_places=5,
                default=0,
                help_text="Set to zero when: Unused / Defined in other contract / Not applicable to your situation",
                max_digits=11,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Fixed daily costs (€)",
            ),
        ),
        migrations.AlterField(
            model_name="energysupplierprice",
            name="gas_price",
            field=models.DecimalField(
                decimal_places=5,
                default=0,
                help_text="Set to zero when: Unused / Defined in other contract / Not applicable to your situation",
                max_digits=11,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Gas price (€)",
            ),
        ),
        migrations.AlterField(
            model_name="energysupplierprice",
            name="start",
            field=models.DateField(db_index=True, verbose_name="Contract start"),
        ),
        migrations.AlterUniqueTogether(
            name="energysupplierprice",
            unique_together=set(),
        ),
    ]

    dependencies = [
        ("dsmr_consumption", "0016_fixed_daily_cost"),
    ]
