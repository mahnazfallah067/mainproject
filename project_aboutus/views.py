from django.shortcuts import render

from project_blog.models import Blog
from .models import AboutUs
# Create your views here.


def about_us(request):
    aboutus = AboutUs.objects.all()
    latest_product = Blog.objects.order_by('-id').all()[:3]
    context = {
        'aboutus': aboutus,
        'latest_product': latest_product
    }
    return render(request, 'about_us.html', context)