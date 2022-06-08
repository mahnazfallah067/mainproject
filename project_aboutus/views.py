from django.shortcuts import render
from .models import AboutUs
# Create your views here.


def about_us(request):
    aboutus = AboutUs.objects.all()
    context = {
        'aboutus': aboutus
    }
    return render(request, 'about_us.html', context)