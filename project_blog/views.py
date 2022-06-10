from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog

# Create your views here.


class BlogListView(ListView):
    template_name = 'blog.html'
    paginate_by = 2

    def get_queryset(self):
        return Blog.objects.all()




