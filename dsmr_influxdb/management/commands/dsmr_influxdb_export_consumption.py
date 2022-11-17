import pickle  # noqa: S403
import logging
import codecs

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from dsmr_influxdb.models import InfluxdbIntegrationSettings, InfluxdbMeasurement
import dsmr_influxdb.services


logger = logging.getLogger("dsmrreader")


class Command(BaseCommand):
    help = "Exports historic readings to the InfluxDB bucket specified as argument"

    def handle(self, **options):
        """Processes queued measurements."""

        self.influxdb_client = dsmr_influxdb.services.initialize_client()

        selection = InfluxdbMeasurement.objects.all().order_by("-pk")[
            0 : settings.DSMRREADER_INFLUXDB_MAX_MEASUREMENTS_IN_QUEUE
        ]

        influxdb_settings = InfluxdbIntegrationSettings.get_solo()

        # Integration disabled.
        if not influxdb_settings.enabled:
            raise CommandError("InfluxDB integration is disabled")

        if not selection:
            logger.info("INFLUXDB: No InfluxDB measurement objects to export, returning")
            return

        logger.info("INFLUXDB: Processing %d measurement(s)", len(selection))
        influxdb_settings = InfluxdbIntegrationSettings.get_solo()

        for current in selection:
            try:
                decoded_fields = codecs.decode(current.fields.encode(), "base64")
                unpickled_fields = pickle.loads(decoded_fields)  # noqa: S301

                with self.influxdb_client.write_api(write_options=SYNCHRONOUS) as write_api:
                    write_api.write(
                        bucket=influxdb_settings.bucket,
                        org=influxdb_settings.organization,
                        record={
                            "measurement": current.measurement_name,
                            "time": current.time,
                            "fields": unpickled_fields,
                        },
                    )
            except Exception as error:
                logger.error(
                    "INFLUXDB: Writing measurement(s) failed: %s, data: %s",
                    error,
                    current.fields,
                )

            current.delete()

        # This purges the remainder.
        InfluxdbMeasurement.objects.all().delete()
