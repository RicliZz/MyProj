from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request):
    context = {
        'title': 'Главная страница',
        'content': 'Содержание главной страницы'
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')