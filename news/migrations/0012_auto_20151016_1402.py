# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_comment_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.CharField(default=None, max_length=120, verbose_name='\u5185\u5bb9'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ip',
            field=models.GenericIPAddressField(default=None, null=True, verbose_name='IP\u5730\u5740', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='vote_ups',
            field=models.IntegerField(default=0, verbose_name='\u9876'),
        ),
    ]
