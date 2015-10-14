# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_short_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_type',
            field=models.CharField(default=b'others', max_length=20, choices=[(b'science', '\u79d1\u6280'), (b'society', '\u793e\u4f1a'), (b'entertainment', '\u5a31\u4e50'), (b'sports', '\u4f53\u80b2'), (b'others', '\u5176\u4ed6')]),
        ),
    ]
