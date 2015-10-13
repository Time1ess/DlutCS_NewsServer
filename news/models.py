# -*- coding:gb18030 -*-
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class News(models.Model):
    title=models.CharField(u'����',max_length=128,null=False,blank=False)
    picture=models.ImageField(upload_to='news_pics',blank=True)
    pub_date=models.DateTimeField(u'����ʱ��',default=timezone.now)
    author=models.CharField(u'����',max_length=60,default=u'��')
    views=models.IntegerField(u'�������',default=0)
    likes=models.IntegerField(u'ϲ������',default=0)
    source=models.CharField(u'��Դ',max_length=60,default=u'��վ')
    content=RichTextField(u'����')
    short_content=models.CharField(u'ժҪ',max_length=120,default=None)

    def __unicode__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.short_content=self.short_content[:90]+'...'
        super(News,self).save(*args,**kwargs)
