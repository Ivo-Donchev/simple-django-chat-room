# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='added',
            field=models.BooleanField(default=False),
        ),
    ]