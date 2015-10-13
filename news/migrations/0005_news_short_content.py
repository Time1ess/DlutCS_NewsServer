# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20151013_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='short_content',
            field=models.CharField(default=None, max_length=120, verbose_name='\u6458\u8981'),
        ),
    ]
