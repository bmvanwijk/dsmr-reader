# Generated by Django 3.2.11 on 2022-01-25 22:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dsmr_backup", "0013_dropbox_setting_refactoring"),
    ]

    operations = [
        migrations.AddField(
            model_name="dropboxsettings",
            name="app_key",
            field=models.CharField(
                blank=True,
                default=None,
                help_text='The "App Key" of the App in Dropbox to use (should be the "Official DSMR-reader" App Key)',
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="dropboxsettings",
            name="one_time_authorization_code",
            field=models.CharField(
                blank=True,
                default=None,
                verbose_name="Access Code by Dropbox",
                help_text="Enter the one-time Access Code here that Dropbox generates for you after authorizing DSMR-reader",
                max_length=255,
                null=True,
            ),
        ),
        migrations.RemoveField(
            model_name="dropboxsettings",
            name="access_token",
        ),
        migrations.AddField(
            model_name="dropboxsettings",
            name="refresh_token",
            field=models.CharField(
                blank=True,
                default=None,
                help_text="Automatically managed by DSMR-reader",
                max_length=255,
                null=True,
                verbose_name="Dropbox refresh token",
            ),
        ),
        migrations.AddField(
            model_name="dropboxsettings",
            name="serialized_auth_flow",
            field=models.BinaryField(
                blank=True,
                default=None,
                help_text="Automatically managed by DSMR-reader - Only used once during authorization set up",
                null=True,
            ),
        ),
    ]
