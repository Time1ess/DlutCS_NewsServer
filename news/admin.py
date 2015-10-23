from django.contrib import admin

from .models import News,Comment

class NewsAdmin(admin.ModelAdmin):
    list_display=('id','title','pub_date','author','source','views','comments')
    list_filter=['pub_date','source','author']
    search_fields=['title','source','author']
    exclude=('short_content',)

class CommentAdmin(admin.ModelAdmin):
    list_display=('id','author','news','pub_date','ip','short_content','vote_ups')
    list_filter=['pub_date']
    search_fields=['author','news','ip','content']

admin.site.register(News,NewsAdmin)
admin.site.register(Comment,CommentAdmin)
