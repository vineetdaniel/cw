# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 06:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_auto_20170129_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='vehicle_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicles.VehicleType'),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='type',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
