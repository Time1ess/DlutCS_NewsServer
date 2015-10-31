#DLUT News Server-新闻服务器

========================
# About

 * DLUT CS Software Comprehensive Practice
 * Branchs:
    - Master:stable branch
    - dev：team develop branch
    - dev-[NAME]：personal develop branch

# Enviroment

- Python 2.7.9
- MySQL 5.6
- Django==1.8.5
- Pillow==3.0.0
- coverage==4.0
- django-ckeditor==5.0.2
- django-grappelli==2.7.2

# How to install

1. execute this in terminal:**sudo pip install -r requirements.txt**
2. create database in mysql:create database newsserver character SET utf8;
3. migrate the database:python manage.py migrate
4. start server:python manage.py runserver IP:PORT
5. visit in your web browser:http://IP:PORT/news

# Structure

```
DlutCS_NewsServer
./DlutCS_NewsServer  Django Settings
./media              medias
./media/news_pics    news thumbnails
./news               news app MVC
./news/models.py     news models
./news/tests.py      news tests
./news/views.py      news views
./news/urls.py       news mappings
./news/static        news static files(includ js,css)
./templates          news templates
```

# Licenses
This software users **GPLv3** lincense,Our team own the copyright.




