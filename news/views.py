# -*- coding:gb18030 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import News

def index(request):
    news=News.objects.all()
    hot_news=News.objects.all().order_by('-views')[:3]
    favorite_news=News.objects.all().order_by('-likes')[:3]
    return render(request,'news/index.html',{
        'news':news,
        'hot_news':hot_news,
        'favorite_news':favorite_news
        })

def news(request):
    news_id=request.GET['id']
    try:
        news=News.objects.get(id=news_id)
        return render(request,'news/news.html',{
            'news':news,
            })
    except:
        return render(request,'news/news.html',{
            'news':None,
            })

def about(request):
    hot_news=News.objects.all().order_by('-views')[:3]
    favorite_news=News.objects.all().order_by('-likes')[:3]
    return render(request,'news/about.html',{
        'hot_news':hot_news,
        'favorite_news':favorite_news})
