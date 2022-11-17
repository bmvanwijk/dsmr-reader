from decimal import Decimal
from unittest import mock

from django.test import TestCase, override_settings
from django.utils import timezone
from influxdb_client import InfluxDBClient

from dsmr_backend.tests.mixins import InterceptCommandStdoutMixin
from dsmr_consumption.models.consumption import ElectricityConsumption
from dsmr_influxdb.models import InfluxdbIntegrationSettings, InfluxdbMeasurement
import dsmr_influxdb.services


class TestCases(InterceptCommandStdoutMixin, TestCase):
    fixtures = ["dsmr_influxdb/measurements.json"]

    def setUp(self):
        InfluxdbIntegrationSettings.get_solo()
        InfluxdbIntegrationSettings.objects.update(enabled=True)

        self.reading = ElectricityConsumption.objects.create(
            read_at=timezone.now(),
            delivered_1=1,
            returned_1=2,
            delivered_2=3,
            returned_2=4,
            currently_delivered=5,
            currently_returned=6,
            phase_currently_delivered_l1=7,
            phase_currently_delivered_l2=8,
            phase_currently_delivered_l3=9,
            phase_currently_returned_l1=10,
            phase_currently_returned_l2=11,
            phase_currently_returned_l3=12,
            phase_voltage_l1=13,
            phase_voltage_l2=14,
            phase_voltage_l3=15,
            phase_power_current_l1=16,
            phase_power_current_l2=17,
            phase_power_current_l3=18,
        )

    def test_initialize_client_disabled(self):
        InfluxdbIntegrationSettings.objects.update(enabled=False)

        client = dsmr_influxdb.services.initialize_client()
        self.assertIsNone(client)

    @mock.patch("influxdb_client.client.bucket_api.BucketsApi.find_bucket_by_name")
    @mock.patch("influxdb_client.client.bucket_api.BucketsApi.create_bucket")
    def test_initialize_client_connection_error(
        self, create_bucket_mock, find_bucket_mock
    ):
        find_bucket_mock.return_value = None
        create_bucket_mock.side_effect = RuntimeError("Connection failed")

        with self.assertRaises(RuntimeError):
            dsmr_influxdb.services.initialize_client()

    @mock.patch("influxdb_client.client.bucket_api.BucketsApi.find_bucket_by_name")
    @mock.patch("influxdb_client.client.bucket_api.BucketsApi.create_bucket")
    def test_initialize_client_default(self, create_bucket_mock, find_bucket_mock):
        find_bucket_mock.return_value = None
        self.assertFalse(create_bucket_mock.called)

        client = dsmr_influxdb.services.initialize_client()
        self.assertIsNotNone(client)
        self.assertTrue(create_bucket_mock.called)
        self.assertTrue(client.url.startswith("http://"))

    @mock.patch("influxdb_client.client.bucket_api.BucketsApi.find_bucket_by_name")
    @mock.patch("influxdb_client.client.bucket_api.BucketsApi.create_bucket")
    def test_initialize_client_secure_unverified(
        self, create_bucket_mock, find_bucket_mock
    ):
        find_bucket_mock.return_value = None
        InfluxdbIntegrationSettings.objects.update(
            secure=InfluxdbIntegrationSettings.SECURE_CERT_NONE
        )
        self.assertFalse(create_bucket_mock.called)

        client = dsmr_influxdb.services.initialize_client()
        self.assertIsNotNone(client)
        self.assertTrue(create_bucket_mock.called)
        self.assertTrue(client.url.startswith("https://"))

    @mock.patch("influxdb_client.client.bucket_api.BucketsApi.find_bucket_by_name")
    @mock.patch("influxdb_client.client.bucket_api.BucketsApi.create_bucket")
    def test_initialize_client_secure_verify_ssl(
        self, create_bucket_mock, find_bucket_mock
    ):
        find_bucket_mock.return_value = None
        InfluxdbIntegrationSettings.objects.update(
            secure=InfluxdbIntegrationSettings.SECURE_CERT_REQUIRED
        )
        self.assertFalse(create_bucket_mock.called)

        client = dsmr_influxdb.services.initialize_client()
        self.assertIsNotNone(client)
        self.assertTrue(create_bucket_mock.called)
        self.assertTrue(client.url.startswith("https://"))

    @mock.patch("influxdb_client.client.write_api.WriteApi.write")
    def test_run_empty(self, write_points_mock):
        InfluxdbMeasurement.objects.all().delete()

        dsmr_influxdb.services.run(InfluxDBClient("http://localhost:8086", ""))
        self.assertFalse(write_points_mock.called)  # Not reached.

    @mock.patch("influxdb_client.client.write_api.WriteApi.write")
    def test_run_exception(self, write_points_mock):
        write_points_mock.side_effect = RuntimeError("Explosion")

        dsmr_influxdb.services.run(InfluxDBClient("http://localhost:8086", ""))

        self.assertEqual(InfluxdbMeasurement.objects.count(), 3)

    @mock.patch("influxdb_client.client.write_api.WriteApi.write")
    def test_run(self, write_points_mock):
        self.assertFalse(write_points_mock.called)
        self.assertEqual(InfluxdbMeasurement.objects.count(), 3)

        dsmr_influxdb.services.run(InfluxDBClient("http://localhost:8086", ""))
        self.assertTrue(write_points_mock.called)
        self.assertEqual(write_points_mock.call_count, 3)
        self.assertEqual(InfluxdbMeasurement.objects.count(), 3)

    @override_settings(DSMRREADER_INFLUXDB_MAX_MEASUREMENTS_IN_QUEUE=1)
    @mock.patch("influxdb_client.client.write_api.WriteApi.write")
    def test_run_overrun(self, write_points_mock):
        """More measurements stored than we're allowed to process."""
        self.assertFalse(write_points_mock.called)

        dsmr_influxdb.services.run(InfluxDBClient("http://localhost:8086", ""))

        self.assertTrue(write_points_mock.called)
        self.assertEqual(write_points_mock.call_count, 1)  # Only once
        self.assertEqual(InfluxdbMeasurement.objects.count(), 3)

    def test_publish_consumption_disabled(self):
        InfluxdbIntegrationSettings.objects.update(enabled=False)

        InfluxdbMeasurement.objects.all().delete()
        self.assertEqual(InfluxdbMeasurement.objects.count(), 0)

        dsmr_influxdb.services.publish_e_consumption(self.reading)

        # Still nothing, because it's blocked.
        self.assertEqual(InfluxdbMeasurement.objects.count(), 0)

    def test_publish_consumption(self):
        InfluxdbMeasurement.objects.all().delete()
        self.assertEqual(InfluxdbMeasurement.objects.count(), 0)

        dsmr_influxdb.services.publish_e_consumption(self.reading)

        # Assumes default mapping.
        self.assertEqual(InfluxdbMeasurement.objects.count(), 3)
        self.assertTrue(
            InfluxdbMeasurement.objects.filter(
                measurement_name="electricity_voltage"
            ).exists()
        )
        self.assertTrue(
            InfluxdbMeasurement.objects.filter(
                measurement_name="electricity_phases"
            ).exists()
        )
        self.assertTrue(
            InfluxdbMeasurement.objects.filter(
                measurement_name="electricity_power"
            ).exists()
        )

    @mock.patch("logging.Logger.warning")
    def test_publish_consumption_invalid_mapping(self, warning_logger_mock):
        InfluxdbIntegrationSettings.objects.update(
            formatting="""
[fake]
non_existing_field = whatever
"""
        )

        InfluxdbMeasurement.objects.all().delete()
        self.assertEqual(InfluxdbMeasurement.objects.count(), 0)

        dsmr_influxdb.services.publish_e_consumption(self.reading)

        # Invalid mapping.
        self.assertEqual(InfluxdbMeasurement.objects.count(), 0)
        self.assertFalse(
            InfluxdbMeasurement.objects.filter(measurement_name="fake").exists()
        )
        self.assertTrue(warning_logger_mock.callled)
