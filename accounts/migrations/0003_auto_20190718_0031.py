# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-17 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190718_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Country_name', models.CharField(default=0, max_length=20)),
                ('Country_code', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Coffee',
        ),
    ]
