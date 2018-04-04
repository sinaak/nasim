# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allinone', '0004_auto_20150921_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesssoriesphoto',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='images/accesssories')),
                ('Model', models.IntegerField(default=1, choices=[(1, 'Necklace'), (2, 'Bracelet '), (3, 'Earring'), (4, 'Others')])),
                ('is_available', models.BooleanField()),
                ('year', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='firstpageimage',
            name='image',
            field=models.ImageField(upload_to='images/firstpageslideshow/'),
        ),
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(upload_to='images/news'),
        ),
    ]
