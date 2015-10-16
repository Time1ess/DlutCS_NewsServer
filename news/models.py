# -*- coding:gb18030 -*-
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from get_short_content import ContentParser
from django.contrib.auth.models import User

news_types=(
        (u'�Ƽ�',u'�Ƽ�'),
        (u'���',u'���'),
        (u'����',u'����'),
        (u'����',u'����'),
        (u'����',u'����'),
        )

class News(models.Model):
    title=models.CharField(u'����',max_length=128,null=False,blank=False)
    picture=models.ImageField(u'����ͼ',upload_to='news_pics',blank=True)
    pub_date=models.DateTimeField(u'����ʱ��',default=timezone.now)
    author=models.CharField(u'����',max_length=60,default=u'��')
    views=models.IntegerField(u'�������',default=0)
    comments=models.IntegerField(u'������',default=0)
    source=models.CharField(u'��Դ',max_length=60,default=u'��վ')
    content=RichTextField(u'����')
    short_content=models.CharField(u'ժҪ',max_length=120,default=None)
    news_type=models.CharField(u'����',max_length=20,choices=news_types,default=u'����')
    top_line=models.BooleanField(u'ͷ��',default=None)

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
    pub_date=models.DateTimeField(u'����ʱ��',default=timezone.now)
    ip=models.GenericIPAddressField(u'IP��ַ',default=None,blank=True,null=True)
    content=models.CharField(u'����',max_length=120,default=None,blank=False,null=False)
    reply_to=models.ForeignKey('self',blank=True,null=True)
    vote_ups=models.IntegerField(u'��',default=0)

    def __unicode__(self):
        return self.short_content()

    def short_content(self):
        return self.content[:20]




