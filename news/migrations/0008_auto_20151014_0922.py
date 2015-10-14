# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20151014_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='top_line',
            field=models.BooleanField(default=None, verbose_name='\u5934\u6761'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_type',
            field=models.CharField(default='\u5176\u4ed6', max_length=20, verbose_name='\u7c7b\u578b', choices=[('\u79d1\u6280', '\u79d1\u6280'), ('\u793e\u4f1a', '\u793e\u4f1a'), ('\u5a31\u4e50', '\u5a31\u4e50'), ('\u4f53\u80b2', '\u4f53\u80b2'), ('\u5176\u4ed6', '\u5176\u4ed6')]),
        ),
    ]
