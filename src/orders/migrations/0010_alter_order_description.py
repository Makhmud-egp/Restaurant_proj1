# Generated by Django 5.1.3 on 2024-12-25 11:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]