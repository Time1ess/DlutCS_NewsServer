# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20151023_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='picture',
            field=models.ImageField(default=b'news_pics/default.jpg', upload_to=b'news_pics', verbose_name='\u7f29\u7565\u56fe', blank=True),
        ),
    ]
