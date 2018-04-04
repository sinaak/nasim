# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allinone', '0002_auto_20150903_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothsphoto',
            name='Model',
            field=models.IntegerField(default=1, choices=[(1, 'OutWear'), (2, 'Ready To Wear '), (3, 'Haute Couture'), (4, 'Shawl'), (5, 'Others')]),
        ),
    ]
