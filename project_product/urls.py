from django.urls import path
from .views import product_list, product_detail
urlpatterns = [
    path('product', product_list),
    path('product/<id>', product_detail, name='productdetail')



]
