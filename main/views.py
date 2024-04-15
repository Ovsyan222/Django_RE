from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict[str,str] = {
        'title': 'Главная',
        'content': 'Магазин ремонтного оборудования :RE'
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict[str,str] = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': "Просто текст"
    }

    return render(request, 'main/about.html', context)
