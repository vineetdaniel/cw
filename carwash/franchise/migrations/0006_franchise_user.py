# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 03:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('franchise', '0005_auto_20170202_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='franchise',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
