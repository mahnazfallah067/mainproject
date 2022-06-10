from django.shortcuts import render
from .models import ReSearche
from project_slider_research.models import SliderResearch

# Create your views here.


def re_search(request):
    research = ReSearche.objects.all()
    slider = SliderResearch.objects.all()
    context = {
        'research': research,
        'slider': slider
    }
    return render(request, 'research.html', context)


def research_detail(request, id):
    detail = ReSearche.objects.get(id=id)
    slider = SliderResearch.objects.all()
    context = {
        'detail': detail,
        'slider': slider
    }
    return render(request, 'research_detail.html', context)
