# Generated by Django 3.2.7 on 2021-10-30 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0002_alter_user_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
