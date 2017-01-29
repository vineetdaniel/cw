# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.PositiveIntegerField()),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField()),
            ],
            options={
                'ordering': ('pincode', 'city'),
            },
        ),
    ]