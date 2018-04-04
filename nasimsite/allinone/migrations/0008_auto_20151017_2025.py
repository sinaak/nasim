# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import embed_video.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('allinone', '0007_feedbacksuggestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='Model',
            field=models.IntegerField(choices=[(1, 'ax'), (2, 'videos')], default=1),
        ),
        migrations.AddField(
            model_name='new',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=datetime.datetime(2015, 10, 17, 20, 25, 37, 699355, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instagramimage',
            name='image',
            field=models.ImageField(upload_to='images/instagramimages/'),
        ),
    ]
