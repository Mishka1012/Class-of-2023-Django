# Class of 2023 Django Grodno Python IT Academy

Django — это высокоуровневая веб-инфраструктура Python, которая позволяет быстро разрабатывать безопасные и удобные в обслуживании веб-сайты. Вот учебник для начинающих по Django 4.0:

1. Установка: Сначала вам нужно установить Django на вашу систему. Вы можете сделать это, выполнив следующую команду в терминале:
```shell
pipenv install django~=4.0
```
2. Создать проект: Чтобы создать новый проект Django, выполните следующую команду:
```shell
django-admin startproject projectname
```
Замените `projectname` на имя вашего проекта.
3. Запустить сервер разработки: Перейдите в директорию проекта и выполните следующую команду:
```shell
python manage.py runserver
```
Это запустит сервер разработки на порте по умолчанию (8000). Вы можете получить доступ к серверу, посетив http://127.0.0.1:8000/ в вашем веб-браузере.
4. Создать приложение: Чтобы создать новое приложение Django, выполните следующую команду:
```shell
python manage.py startapp appname
```
Замените 'appname' на имя вашего приложения.
5. Определить модель: Модель - это представление таблицы базы данных в Django. Вы можете определить модель в файле models.py вашего приложения. Например:
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
```
6. Миграция базы данных: Чтобы создать таблицы базы данных для ваших моделей, выполните следующие команды:
```shell
python manage.py makemigrations
python manage.py migrate
```
7. Создать представление: Представление - это функция Python, которая обрабатывает запросы HTTP и возвращает ответ HTTP. Вы можете создавать представления в файле views.py вашего приложения. Например:
```python
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
```
8. Создать шаблон URL: Шаблон URL сопоставляет URL с представлением в Django. Вы можете создавать шаблоны URL в файле urls.py вашего приложения. Например:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
]
```
9. Создать шаблон: Шаблон - это файл HTML, который определяет структуру веб-страницы. Вы можете создавать шаблоны в директории templates вашего приложения. Например:
```html
<html>
  <head>
    <title>Список книг</title>
  </head>
  <body>
    <h1>Список книг</h1>
    <ul>
      {% for book in books %}
        <li>{{ book.title }} автор {{ book.author }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```
Это только базовое введение в Django. Вы можете найти более подробную информацию и учебные пособия на сайте Django: https://djangoproject.com/

# Защите

- Расказать о себе
- Показать проект
  - Рабочая сторона
  - код
- Вопросы

# Требования к финальному проекту

- Тесты
- Деплой
- Проект работает
- Защита
- Пользователи
- 