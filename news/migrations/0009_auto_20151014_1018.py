# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20151014_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='likes',
        ),
        migrations.AddField(
            model_name='news',
            name='comments',
            field=models.IntegerField(default=0, verbose_name='\u8bc4\u8bba\u6570'),
        ),
    ]
