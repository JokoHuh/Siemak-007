# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-13 03:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matakuliah',
            name='prodi',
        ),
        migrations.AddField(
            model_name='matakuliah',
            name='pts',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='db.Pts'),
        ),
    ]