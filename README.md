#DLUT News Server-新闻服务器
软件综合训练
- Master分支:稳定版本分支
- Dev分支：团队开发分支
- Dev-[NAME]分支：个人开发分支

##目录结构
```
DlutCS_NewsServer
./DlutCS_NewsServer  Django设置
./media              媒体文件
./media/news_pics    新闻缩略图
./news               新闻MVC
./news/models.py     新闻相关类
./news/tests.py      新闻测试类
./news/views.py      新闻视图
./news/urls.py       网址映射
./news/static        新闻页面相关静态文件
./templates          页面模板
```

##环境
- Python 2.7.9
- MySQL 5.6
- Django==1.8.5
- Pillow==3.0.0
- coverage==4.0
- django-ckeditor==5.0.2


