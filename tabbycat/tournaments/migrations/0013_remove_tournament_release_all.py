# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0012_auto_20160630_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='release_all',
        ),
    ]
