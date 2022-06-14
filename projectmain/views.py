import itertools

from django.shortcuts import render

from project_blog.models import Blog
from project_questions.models import Questions
from project_slider.models import Slider
from project_product.models import Product
from project_sitesetting.models import SiteSetting
from project_aboutus.models import AboutUs
from project_researche.models import ReSearche


def header(request):
    context = {
    }
    return render(request, 'shared/header.html', context)


def footer(request):
    site_setting = SiteSetting.objects.first()
    latest_product = Blog.objects.order_by('-id').all()[:2]
    about_us = AboutUs.objects.first()
    context = {
        'site_setting': site_setting,
        'latest_product': latest_product,
        'about_us': about_us
    }
    return render(request, 'shared/footer.html', context)


# def mygrouper(n, iterable):
#     args = [iter(iterable)] * n
#     return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    sliders = Slider.objects.all()
    products = Product.objects.all()
    product = Product.objects.order_by('id')[:4]
    about_us = AboutUs.objects.all()
    research = ReSearche.objects.order_by('date')[:3]
    latest_product = Blog.objects.order_by('-id').all()[:3]
    questions = Questions.objects.all()
    context = {
        'sliders': sliders,
        'products': products,
        'product': product,
        'about_us': about_us,
        'research': research,
        'latest_product': latest_product,
        'questions': questions
    }
    return render(request, 'home_page.html', context)