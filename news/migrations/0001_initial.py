# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='\u6807\u9898')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('author', models.CharField(default='\u65e0', max_length=60, verbose_name='\u4f5c\u8005')),
                ('views', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6b21\u6570')),
                ('likes', models.IntegerField(default=0, verbose_name='\u559c\u6b22\u6b21\u6570')),
                ('source', models.CharField(default='\u672c\u7ad9', max_length=60)),
                ('content', ckeditor.fields.RichTextField(verbose_name='\u5185\u5bb9')),
            ],
        ),
    ]
