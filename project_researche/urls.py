from django.urls import path
from .views import re_search, research_detail

urlpatterns = [
    path('re_search', re_search),
    path('research_detail/<id>', research_detail),



]