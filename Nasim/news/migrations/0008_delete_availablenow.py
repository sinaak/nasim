# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_availablenow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Availablenow',
        ),
    ]
