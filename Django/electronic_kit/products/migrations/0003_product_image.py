# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170313_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to='/electronic_kit/static/img/'),
        ),
    ]