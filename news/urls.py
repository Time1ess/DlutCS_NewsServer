from django.conf.urls import url,patterns
from news import views
urlpatterns=[
        url(r'^$',views.index,name='index'),
        url(r'^news/$',views.news,name='news'),
        url(r'^about/$',views.about,name='about'),
        url(r'^comment/$',views.comment,name='comment'),
        url(r'^voteup/$',views.voteup,name='voteup'),
        url(r'^category/$',views.category,name='category'),
        url(r'^hot/$',views.hot,name='hot'),
        ]
		

