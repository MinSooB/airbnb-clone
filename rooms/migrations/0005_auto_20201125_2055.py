# Generated by Django 2.2.17 on 2020-11-25 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20201125_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='houserules',
            new_name='house_rules',
        ),
    ]
