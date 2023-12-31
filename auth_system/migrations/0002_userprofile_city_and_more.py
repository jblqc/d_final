# Generated by Django 4.1.10 on 2023-10-28 03:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth_system", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="city",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="email_verification_token",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="email_verified",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="password_reset_token",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="region",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
