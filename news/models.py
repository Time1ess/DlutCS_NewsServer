# -*- coding:gb18030 -*-
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from get_short_content import ContentParser
from django.contrib.auth.models import User

news_types=(
        (u'科技',u'科技'),
        (u'社会',u'社会'),
        (u'娱乐',u'娱乐'),
        (u'体育',u'体育'),
        (u'其他',u'其他'),
        )

class News(models.Model):
    title=models.CharField(u'标题',max_length=128,null=False,blank=False)
    picture=models.ImageField(u'缩略图',upload_to='news_pics',blank=True)
    pub_date=models.DateTimeField(u'发布时间',default=timezone.now)
    author=models.CharField(u'作者',max_length=60,default=u'无')
    views=models.IntegerField(u'点击次数',default=0)
    comments=models.IntegerField(u'评论数',default=0)
    source=models.CharField(u'来源',max_length=60,default=u'本站')
    content=RichTextField(u'内容')
    short_content=models.CharField(u'摘要',max_length=120,default=None)
    news_type=models.CharField(u'类型',max_length=20,choices=news_types,default=u'其他')
    top_line=models.BooleanField(u'头条',default=None)

    def __unicode__(self):
        return self.title

    def save(self,*args,**kwargs):
        parser=ContentParser()
        parser.feed(self.content)
        self.short_content=parser.data[:70]+'...'
        super(News,self).save(*args,**kwargs)

class Comment(models.Model):
    author=models.ForeignKey(User,default=None)
    news=models.ForeignKey(News,default=None)
    pub_date=models.DateTimeField(u'发布时间',default=timezone.now)
    ip=models.GenericIPAddressField(u'IP地址',default=None,blank=True,null=True)
    content=models.CharField(u'内容',max_length=120,default=None,blank=False,null=False)
    reply_to=models.ForeignKey('self',blank=True,null=True)
    vote_ups=models.IntegerField(u'顶',default=0)

    def __unicode__(self):
        return self.short_content()

    def short_content(self):
        return self.content[:20]




