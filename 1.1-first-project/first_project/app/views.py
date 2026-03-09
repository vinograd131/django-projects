from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),  # добавляем ссылку на time_view
        'Показать содержимое рабочей директории': reverse('workdir')  # добавляем ссылку на workdir_view
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    work_dir = os.getcwd()  # получаем текущую рабочую директорию
    files = os.listdir(work_dir)  # получаем список файлов и папок
    files_list = '<br>'.join(files)  # преобразуем список в строку с переносами
    msg = f'Содержимое рабочей директории:<br>{files_list}'
    return HttpResponse(msg)
