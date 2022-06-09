from project_sitesetting.models import SiteSetting


def context_processor(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'site_setting': site_setting
    }
    return context