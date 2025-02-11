from django.shortcuts import render
from .models import (
    Slider, Advantage, WhoWe, Settings, 
    Stages_of_work, Carts_for_stages_of_work, Text_gallery, Gallery)


def home(request):
    settings = Settings.objects.latest('id')
    slider = Slider.objects.all()
    advent = Advantage.objects.all()
    whowe = WhoWe.objects.latest('-id')
    stages = Stages_of_work.objects.latest('id')
    carts_stages = Carts_for_stages_of_work.objects.all()
    text_gallery = Text_gallery.objects.latest('id')
    gallery = Gallery.objects.all() 
    context = {
        'settings': settings,
        'slider': slider,
        'advent': advent,
        'whowe': whowe,
        'stages': stages,
        'carts_stages': carts_stages,
        'text_gallery': text_gallery,
        'gallery': gallery,
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')