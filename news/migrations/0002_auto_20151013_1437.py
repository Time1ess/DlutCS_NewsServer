# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.CharField(default='\u672c\u7ad9', max_length=60, verbose_name='\u6765\u6e90'),
        ),
    ]
