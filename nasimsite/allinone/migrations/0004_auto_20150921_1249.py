# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allinone', '0003_clothsphoto_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothsphoto',
            name='image',
            field=models.ImageField(upload_to='images/cloths'),
        ),
    ]
