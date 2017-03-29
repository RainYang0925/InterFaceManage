# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserGroup', '0004_usergroup_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='create_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
