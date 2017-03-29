# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('UserGroup', '0003_auto_20170328_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='create_time',
            field=models.DateField(default=datetime.datetime(2017, 3, 28, 10, 10, 39, 134344), blank=True),
            preserve_default=False,
        ),
    ]
