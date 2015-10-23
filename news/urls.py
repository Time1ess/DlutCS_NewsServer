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
        url(r'^user_logout/',views.user_logout,name='user_logout'),
        url(r'^user_login/',views.user_login,name='user_login'),
        url(r'^random_news/',views.random_news,name='random_news'),
        url(r'^query_more/',views.query_more,name='query_more'),
        ]
		

