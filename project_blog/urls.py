from django.urls import path
# from .views import blog
from .views import BlogListView, BlogDetailView
urlpatterns = [
    path('blog', BlogListView.as_view()),
    path('blog-detail/<int:id>/<slug:slug>', BlogDetailView.as_view())
]