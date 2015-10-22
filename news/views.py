# -*- coding:gb18030 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import News,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from random import randint

def index(request):
    title=u'首页'
    news=News.objects.all().order_by('-pub_date')[:10]
    hot_news=News.objects.all().order_by('-views','-pub_date')[:3]
    favorite_news=News.objects.all().order_by('-comments','-pub_date')[:3]
    return render(request,'news/newslist.html',{
        'title':title,
        'news':news,
        'hot_news':hot_news,
        'favorite_news':favorite_news
        })

def category(request):
    news_type=request.GET['news_type']
    if news_type==u'头条':
        category_news=News.objects.filter(top_line=news_type)
    elif news_type==u'首页':
        category_news=News.objects.all()
    else:
        category_news=News.objects.filter(news_type=news_type)
    title=news_type
    hot_news=category_news.order_by('-views','-pub_date')[:3]
    favorite_news=category_news.order_by('-comments','-pub_date')[:3]
    news=category_news.order_by('-pub_date')[:10]
    return render(request,'news/newslist.html',{
        'title':title,
        'hot_news':hot_news,
        'favorite_news':favorite_news,
        'news':news,
        })

def hot(request):
    hot_type=request.GET['hot_type']
    if hot_type==u'热门点击':
        hot_type_news=News.objects.all().order_by('-views','-pub_date')[:10]
    elif hot_type==u'热门评论':
        hot_type_news=News.objects.all().order_by('-comments','-pub_date')[:10]
    title=hot_type
    hot_news=News.objects.all().order_by('-views','-pub_date')[:3]
    favorite_news=News.objects.all().order_by('-comments','-pub_date')[:3]
    return render(request,'news/newslist.html',{
        'title':title,
        'hot_news':hot_news,
        'favorite_news':favorite_news,
        'news':hot_type_news,
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
        comments=Comment.objects.filter(news=news).order_by('-pub_date')
        comments_count=Comment.objects.filter(news=news).count()
        return render(request,'news/news.html',{
            'news':news,
            'hot_news':hot_news,
            'guess_you_like':guess_you_like,
            'favorite_news':favorite_news,
            'relative_news':relative_news,
            'comments':comments,
            'comments_count':comments_count,
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

@login_required
def comment(request):
    if request.method=='GET':
        try:
            author=request.user
            news_id=request.GET['news_id']
            news=News.objects.get(id=news_id)
            ip=request.META['REMOTE_ADDR']
            content=request.GET['content']
            reply_to_id=int(request.GET['reply_to_id'])
            if reply_to_id==0:
                reply_to=None
            else:
                reply_to=Comment.objects.get(id=reply_to_id)
            comment=Comment(author=author,news=news,ip=ip,
                    content=content,reply_to=reply_to)
            comment.save()
            news.comments+=1
            news.save()
            return HttpResponse('SUCCESS')
        except:
            return HttpResponse('try FAIL')
    else:
        return HttpResponse('method FAIL')

@login_required
def voteup(request):
    if request.method=='GET':
        try:
            comment_id=int(request.GET['comment_id'])
            comment=Comment.objects.get(id=comment_id)
            comment.vote_ups+=1
            comment.save()
            return HttpResponse(comment.vote_ups)
        except:
            return HttpResponse('try FAIL')
    else:
        return HttpResponse('method FAIL')

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/news/')

def user_login(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/news/')
            else:
                return render(request,'news/error.html',
                        {
                            'error_message':"用户未激活",
                            })
        else:
            return render(request,'news/error.html',
                    {
                        'error_message':"用户信息错误",
                        })
    else:
        return render(request,'news/login.html',{})
def random_news(request):
    news=News.objects.order_by('?')[:10]
    title=u'随机新闻'
    hot_news=News.objects.all().order_by('-views','-pub_date')[:3]
    favorite_news=News.objects.all().order_by('-comments','-pub_date')[:3]
    return render(request,'news/newslist.html',{
        'title':title,
        'hot_news':hot_news,
        'favorite_news':favorite_news,
        'news':news,
        })
