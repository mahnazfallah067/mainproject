from django.urls import path
# from .views import blog
from .views import BlogListView
urlpatterns = [
    # path('blog', blog)
    path('blog', BlogListView.as_view())
]