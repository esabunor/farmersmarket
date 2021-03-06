# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-17 15:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0004_auto_20160107_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='companyimage',
            field=models.ImageField(blank=True, upload_to='media/partners/companyimage'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='users',
            field=models.ManyToManyField(related_name='partners', to=settings.AUTH_USER_MODEL, verbose_name='Users'),
        ),
    ]
