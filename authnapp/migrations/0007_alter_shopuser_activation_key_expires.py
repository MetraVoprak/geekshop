# Generated by Django 3.2.12 on 2022-04-29 08:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0006_create_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 1, 8, 50, 53, 519937, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
