# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_auto_20171031_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unavailableslot',
            name='day',
            field=models.CharField(max_length=3),
        ),
    ]
