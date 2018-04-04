# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allinone', '0008_auto_20151017_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='Model',
        ),
        migrations.RemoveField(
            model_name='new',
            name='video',
        ),
    ]
