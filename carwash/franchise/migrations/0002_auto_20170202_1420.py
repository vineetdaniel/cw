# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('franchise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='franchise',
            name='members',
        ),
        migrations.RemoveField(
            model_name='services',
            name='group',
        ),
        migrations.AddField(
            model_name='services',
            name='franchise',
            field=models.ManyToManyField(to='franchise.Franchise'),
        ),
    ]
