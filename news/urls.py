from django.conf.urls import url,patterns
from news import views
urlpatterns=[
        url(r'^$',views.index,name='index'),
        url(r'^news/$',views.news,name='news'),
        url(r'^about/$',views.about,name='about'),
        url(r'^top_line/$',views.top_line,name='top_line'),
        url(r'^comment/$',views.comment,name='comment'),
        ]
		

