# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0012_auto_20160128_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='debit_or_credit',
            field=models.BooleanField(default=False),
        ),
    ]
