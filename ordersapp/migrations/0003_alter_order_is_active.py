# Generated by Django 3.2.12 on 2022-05-04 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ordersapp", "0002_alter_order_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="активен"),
        ),
    ]
