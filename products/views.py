from django.shortcuts import render
from .models import Slider, Advantage, WhoWe, Settings


def home(request):
    settings = Settings.objects.all()
    slider = Slider.objects.all()
    advent = Advantage.objects.all()
    whowe = WhoWe.objects.all()
    context = {
        'settings': settings,
        'slider': slider,
        'advent': advent,
        'whowe': whowe,
    }
    return render(request, 'index.html', context)