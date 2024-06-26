from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    context: dict[str,str] = {
        'title': 'Главная',
        'content': 'Магазин ремонтного оборудования :RE',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict[str,str] = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': "Мы - команда профессионалов в сфере ремонтного оборудования. Наш магазин предоставляет широкий ассортимент товаров для выполнения любых ремонтных работ - от строительных инструментов до электротехники.",
        'text_on_page': "Мы работаем только с проверенными поставщиками, чтобы гарантировать качество и надежность нашей продукции. Наша цель - помочь вам сделать ремонт быстрым, эффективным и безопасным. ",
        'text_on_page': "У нас вы найдете все необходимое для ремонта дома, квартиры или офиса, а также для работы на строительной площадке. Наш опытный персонал всегда готов помочь вам выбрать подходящее оборудование и ответить на все ваши вопросы. Мы стремимся к тому, чтобы наш магазин был вашим надежным партнером во всех ваших ремонтных проектах. С нами вы можете быть уверены в качестве товаров и профессиональном обслуживании. Доверьте свой ремонт нам и мы поможем вам сделать его легким и приятным процессом!",
    }

    return render(request, 'main/about.html', context)
