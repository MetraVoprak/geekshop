# Generated by Django 3.2.12 on 2022-05-03 10:12

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0008_alter_shopuser_activation_key_expires"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 5, 5, 10, 12, 21, 626970, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
    ]
