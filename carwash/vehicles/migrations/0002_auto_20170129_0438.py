# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 04:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='brand_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.Brand'),
        ),
    ]
