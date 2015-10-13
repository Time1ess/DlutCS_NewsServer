from django.conf.urls import url,patterns
from news import views
urlpatterns=[
        url(r'^$',views.index,name='index'),
        ]
		

