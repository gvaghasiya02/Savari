# Generated by Django 3.2.7 on 2021-09-29 04:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_auto_20210929_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivertrip',
            name='Vehicle_Number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Vehicle number must be entered in the format: MH-03-C-3843', regex='^[A-Z]{2}[-][0-9]{1,2}[-][A-Z]{1,2}[-][0-9]{3,4}$')]),
        ),
    ]