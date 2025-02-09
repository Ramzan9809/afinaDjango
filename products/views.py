from django.shortcuts import render
from .models import Slider, Advantage, WhoWe


def home(request):
    slider = Slider.objects.all()
    advent = Advantage.objects.all()
    whowe = WhoWe.objects.all()
    context = {
        'slider': slider,
        'advent': advent,
        'whowe': whowe,
    }
    return render(request, 'index.html', context)