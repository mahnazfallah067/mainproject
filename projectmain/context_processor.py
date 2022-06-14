from project_aboutus.models import AboutUs
from project_blog.models import Blog
from project_sitesetting.models import SiteSetting


def context_processor(request):
    site_setting = SiteSetting.objects.first()
    latest_product = Blog.objects.order_by('-id').all()[:2]
    about_us = AboutUs.objects.first()
    context = {
        'site_setting': site_setting,
        'latest_product': latest_product,
        'about_us': about_us
    }
    return context