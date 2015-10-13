# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20151013_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='picture',
            field=models.ImageField(upload_to=b'/news/news_pics', blank=True),
        ),
    ]
