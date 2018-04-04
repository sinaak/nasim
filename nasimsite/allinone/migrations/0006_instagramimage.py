# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allinone', '0005_auto_20150924_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagramimage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'images/instagramimages/')),
            ],
        ),
    ]
