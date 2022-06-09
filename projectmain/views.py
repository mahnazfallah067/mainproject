import itertools

from django.shortcuts import render
from project_slider.models import Slider
from project_product.models import Product
from project_sitesetting.models import SiteSetting


def header(request):
    context = {
    }
    return render(request, 'shared/header.html', context)


def footer(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'site_setting': site_setting
    }
    return render(request, 'shared/footer.html', context)


def mygrouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    sliders = Slider.objects.all()
    products = Product.objects.all()
    product = Product.objects.order_by('id').all()[:8]
    context = {
        'sliders': sliders,
        'products': products,
        'product': mygrouper(2, product)
    }
    return render(request, 'home_page.html', context)