# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserGroup', '0002_auto_20170328_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='login_token',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
