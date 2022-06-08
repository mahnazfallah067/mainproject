from django.shortcuts import render
from .models import Product
from project_slider_andishkadeh.models import SliderAndishkadeh
# Create your views here.


def product_list(request):
    products = Product.objects.all()
    sliders = SliderAndishkadeh.objects.all()
    context = {
        'products': products,
        'sliders': sliders
    }
    return render(request, 'product_list.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    products = Product.objects.all()
    sliders = SliderAndishkadeh.objects.all()
    context = {
        'product': product,
        'products': products,
        'sliders': sliders
    }
    return render(request, 'product_detail.html', context)








