# -*- coding:gb18030 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import News,Comment

def index(request):
    title=u'��ҳ'
    news=News.objects.all().order_by('-pub_date')[:10]
    hot_news=News.objects.all().order_by('-views','-pub_date')[:3]
    favorite_news=News.objects.all().order_by('-comments','-pub_date')[:3]
    return render(request,'news/newslist.html',{
        'title':title,
        'news':news,
        'hot_news':hot_news,
        'favorite_news':favorite_news
        })

def news(request):
    news_id=request.GET['id']
    try:
        news=News.objects.get(id=news_id)
        news_type=news.news_type
        guess_you_like=News.objects.exclude(id=news_id).filter(news_type=news_type).order_by('-comments','-pub_date')[:5]
        relative_news=News.objects.exclude(id=news_id).filter(news_type=news_type).order_by('-pub_date')[:5]
        hot_news=News.objects.all().order_by('-views','-pub_date')[:3]
        favorite_news=News.objects.all().order_by('-comments','-pub_date')[:3]
        news.views+=1
        news.save()
        comments=Comment.objects.filter(news=news).order_by('-pub_date')[:5]
        return render(request,'news/news.html',{
            'news':news,
            'hot_news':hot_news,
            'guess_you_like':guess_you_like,
            'favorite_news':favorite_news,
            'relative_news':relative_news,
            'comments':comments,
            })
    except:
        return render(request,'news/news.html',{
            'news':None,
            })

def about(request):
    hot_news=News.objects.all().order_by('-views','-pub_date')[:3]
    favorite_news=News.objects.all().order_by('-comments','-pub_date')[:3]
    return render(request,'news/about.html',{
        'hot_news':hot_news,
        'favorite_news':favorite_news})

def top_line(request):
    all_top_line_news=News.objects.filter(top_line=True)
    title=u'ͷ��'
    hot_news=all_top_line_news.order_by('-views','-pub_date')[:3]
    favorite_news=all_top_line_news.order_by('-comments','-pub_date')[:3]
    news=all_top_line_news.order_by('-pub_date')[:10]
    return render(request,'news/newslist.html',{
        'title':title,
        'hot_news':hot_news,
        'favorite_news':favorite_news,
        'news':news,
        })

