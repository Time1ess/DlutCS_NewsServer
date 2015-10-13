# -*- coding:gb18030 -*-
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class News(models.Model):
    title=models.CharField(u'标题',max_length=128,null=False,blank=False)
    picture=models.ImageField(upload_to='news_pics',blank=True)
    pub_date=models.DateTimeField(u'发布时间',default=timezone.now)
    author=models.CharField(u'作者',max_length=60,default=u'无')
    views=models.IntegerField(u'点击次数',default=0)
    likes=models.IntegerField(u'喜欢次数',default=0)
    source=models.CharField(u'来源',max_length=60,default=u'本站')
    content=RichTextField(u'内容')
    short_content=models.CharField(u'摘要',max_length=120,default=None)

    def __unicode__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.short_content=self.short_content[:90]+'...'
        super(News,self).save(*args,**kwargs)

