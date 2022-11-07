from unittest import mock

from django.test import TestCase
from django.utils import timezone
from influxdb_client import InfluxDBClient

from dsmr_backend.signals import (
    initialize_persistent_client,
    run_persistent_client,
    terminate_persistent_client,
)
from dsmr_backend.tests.mixins import InterceptCommandStdoutMixin
from dsmr_consumption.models.consumption import ElectricityConsumption
from dsmr_consumption.signals import consumption_created
from dsmr_influxdb.models import InfluxdbIntegrationSettings


class TestCases(InterceptCommandStdoutMixin, TestCase):
    @mock.patch("dsmr_influxdb.services.initialize_client")
    def test_initialize_persistent_client_signal(self, initialize_mock):
        initialize_mock.return_value = None

        self.assertFalse(initialize_mock.called)
        initialize_persistent_client.send_robust(None)
        self.assertTrue(initialize_mock.called)

    @mock.patch("dsmr_influxdb.services.run")
    def test_run_persistent_client_signal(self, run_mock):
        # Invalid client.
        self.assertFalse(run_mock.called)
        run_persistent_client.send_robust(None, client=None)
        self.assertFalse(run_mock.called)

        influxdb_client = InfluxDBClient("http://localhost:8086", "")
        self.assertFalse(run_mock.called)
        run_persistent_client.send_robust(None, client=influxdb_client)
        self.assertTrue(run_mock.called)

    @mock.patch("influxdb_client.InfluxDBClient.close")
    def test_terminate_persistent_client(self, close_mock):
        # Invalid client.
        self.assertFalse(close_mock.called)
        terminate_persistent_client.send_robust(None, client=None)
        self.assertFalse(close_mock.called)

        influxdb_client = InfluxDBClient("http://localhost:8086", "")
        self.assertFalse(close_mock.called)
        terminate_persistent_client.send_robust(None, client=influxdb_client)
        self.assertTrue(close_mock.called)

    @mock.patch("dsmr_backend.signals.backend_restart_required.send_robust")
    def test_restart_required_on_save(self, send_robust_mock):
        """Any change should flag a restart."""
        influxdb_settings = InfluxdbIntegrationSettings.get_solo()
        self.assertFalse(send_robust_mock.called)

        influxdb_settings.hostname = "xxx"
        influxdb_settings.save()
        self.assertTrue(send_robust_mock.called)

        send_robust_mock.reset_mock()
        influxdb_settings.enabled = True
        influxdb_settings.save()
        self.assertTrue(send_robust_mock.called)

    @mock.patch("dsmr_influxdb.services.publish_consumption")
    def test_publish_dsmr_reading_handler(self, publish_dsmr_reading_mock):
        dsmr_reading = ElectricityConsumption.objects.create(
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

        self.assertFalse(publish_dsmr_reading_mock.called)
        consumption_created.send_robust(None, instance=dsmr_reading)
        self.assertTrue(publish_dsmr_reading_mock.called)

        # Trigger error.
        publish_dsmr_reading_mock.side_effect = RuntimeError()
        consumption_created.send_robust(None, instance=dsmr_reading)
        # Should not crash the test.
