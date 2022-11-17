from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from solo.admin import SingletonModelAdmin

from dsmr_backend.mixins import DeletionOnlyAdminModel
from dsmr_influxdb.models import InfluxdbIntegrationSettings, InfluxdbMeasurement


@admin.register(InfluxdbIntegrationSettings)
class InfluxdbIntegrationSettingsAdmin(SingletonModelAdmin):
    save_on_top = True
    change_form_template = "dsmr_influxdb/influxdb_settings/change_form.html"
    fieldsets = (
        (
            None,
            {
                "fields": [
                    "enabled",
                    "hostname",
                    "port",
                    "secure",
                    "organization",
                    "api_token",
                    "bucket",
                ],
                "description": _(
                    "The backend process should automatically restart to apply changes."
                ),
            },
        ),
        (
            _("Mapping_g"),
            {
                "fields": ["formatting_g"],
                "description": """Example:""",
            },
        ),
    )


@admin.register(InfluxdbMeasurement)
class InfluxdbMeasurementAdmin(DeletionOnlyAdminModel):
    list_display = ("time", "measurement_name")
