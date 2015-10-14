from django.contrib import admin

from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display=('id','title','pub_date','author','source','views','comments')
    list_filter=['pub_date','source','author']
    search_fields=['title','source','author']


admin.site.register(News,NewsAdmin)
