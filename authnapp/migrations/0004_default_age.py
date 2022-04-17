# Generated by Django 3.2.12 on 2022-04-17 21:10

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0003_default_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 4, 19, 21, 10, 51, 96285, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
    ]
