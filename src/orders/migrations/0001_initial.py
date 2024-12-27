# Generated by Django 5.1.3 on 2024-12-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(choices=[('Starter', 'Starter'), ('Main', 'Main'), ('Dessert', 'Dessert'), ('Drink', 'Drink')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='orders.menuitem')),
            ],
        ),
    ]