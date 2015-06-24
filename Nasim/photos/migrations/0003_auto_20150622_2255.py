# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20150622_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availablenow',
            name='image',
            field=models.ImageField(upload_to='news/static/images/availablenow'),
        ),
    ]
