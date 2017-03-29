# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('UserGroup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='last_login_time',
            field=models.DateField(default=datetime.datetime(2017, 3, 28, 9, 37, 44, 982337), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usergroup',
            name='login_token',
            field=models.CharField(default=datetime.datetime(2017, 3, 28, 9, 37, 51, 881174), max_length=100),
            preserve_default=False,
        ),
    ]
