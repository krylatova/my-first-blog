from django.conf.urls import url
from . import views

""" Так мы импортировали функцию url Django и все views (представления)
 из приложения blog (у нас их пока нет, но через минуту они появятся!)

После этого мы можем добавить наш первый URL-шаблон
"""

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
"""
Как ты можешь заметить, мы связали view под именем post_list с URL-адресом ^$. 
Это регулярное выражение будет соответствовать ^ (началу) и следующему $ (концу), т.е. пустой строке. 
Это правильно, потому что для обработчиков URL в Django 'http://127.0.0.1:8000/' не является частью URL. 
Этот шаблон скажет Django, что views.post_list — это правильное направление для запроса к твоему веб-сайту 
по адресу 'http://127.0.0.1:8000/'. Последняя часть name='post_list' — это имя URL, которое 
будет использовано, чтобы идентифицировать его. 
Оно может быть таким же, как имя представления (англ. view), а может и чем-то совершенно другим. 
Мы будем использовать именованные URL позднее в проекте, поэтому важно указывать их имена уже сейчас. 
Мы также должны попытаться сохранить имена URL-адресов уникальными и легко запоминающимися.
"""