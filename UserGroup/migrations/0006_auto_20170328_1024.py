# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserGroup', '0005_auto_20170328_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
