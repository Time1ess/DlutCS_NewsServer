from django.conf.urls import url,patterns
from news import views
urlpatterns=[
        url(r'^$',views.index,name='index'),
        url(r'^news/$',views.news,name='news'),
        url(r'^about/$',views.about,name='about'),
        ]
		

