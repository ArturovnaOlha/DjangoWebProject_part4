"""
Definition of views.
"""

from datetime import datetime
import re

from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import AnketaForm
from django.db import models
from .models import Blog

from .models import Comment # использование модели комментариев
from .forms import CommentForm # использование формы ввода комментария

from .forms import BlogForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )



def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Давайте познакомиммся поближе!.',
            'year':datetime.now().year,
        }
    )


def videopost(request):
    """Renders the videopost page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/VIDEOPOST.html',
        {
            'title':'Видосики',
            'message':'Тут есть кое-что интересненькое.',
            'year':datetime.now().year,
        }
    )



def links (request):
    """Renders the link page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/LINKS.html',
        {
            'title':'Полезные ресурсы',
            'message':'Некоторые полезные странички.',
            'year':datetime.now().year,
        }
    )


def ANKETA(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Мужской', '2': 'Женский'}
    audience = {'1': 'Раз в месяц', '2': 'Более одного раза в месяц', '3':'Реже, чем один раз в месяц', '4':'Не посещаю'}
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['job'] = form.cleaned_data['job']
            data['gender'] = gender[form.cleaned_data['gender'] ]
            data['audience'] = audience[form.cleaned_data['audience'] ]
            if(form.cleaned_data['notice'] == True):
                data['notice'] = 'Да'
            else:
                 data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = AnketaForm()
    return render(
        request,
        'app/anketa.html',
        {
            'form':form,
            'data':data
        }
    )


def registration(request):
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST": # после отправки формы

        regform = UserCreationForm (request.POST)

        if regform.is_valid(): #валидация полей формы
          reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
          reg_f.is_staff = False # запрещен вход в административный раздел
          reg_f.is_active = True # активный пользователь
          reg_f.is_superuser = False # не является суперпользователем
          reg_f.date_joined = datetime.now() # дата регистрации
          reg_f.last_login = datetime.now() # дата последней авторизации
          reg_f.save() # сохраняем изменения после добавления данных
          return redirect('home') # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
            'regform': regform, # передача формы в шаблон веб-страницы
            'year':datetime.now().year,
        }

    )


def blog(request):
    """Renders the blog page."""

    posts = Blog.objects.all()  

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title': 'Блог',
            'posts': posts,
            'year': datetime.now().year,
        }
    )



def blogpost(request, parametr):
    """Renders the blogpost page."""
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()

            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()


    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы

            'comments': comments,
            'form': form,

            'year':datetime.now().year,
        }
    )

def newpost(request):
    """Renders the newpost page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()

            return redirect('blog')
    else:
        blogform = BlogForm()

    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': 'Добавить статью блога',
            'year': datetime.now().year,
        
        }
        
    )