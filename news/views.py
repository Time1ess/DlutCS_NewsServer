from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import News

def index(request):
    news=News.objects.all()
    return render(request,'news/index.html',{'news':news})
