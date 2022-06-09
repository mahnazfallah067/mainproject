from django.shortcuts import render
from .forms import CreateContactForm
from .models import ContactUs
from project_sitesetting.models import SiteSetting

# Create your views here.


def contact_page(request):
    contact_form = CreateContactForm(request.POST or None)

    if contact_form.is_valid():
        family = contact_form.cleaned_data.get('family')
        email = contact_form.cleaned_data.get('email')
        text = contact_form.cleaned_data.get('text')
        number = contact_form.cleaned_data.get('number')
        ContactUs.objects.create(family=family, email=email, text=text, number=number)

        contact_form = CreateContactForm()

    site_setting = SiteSetting.objects.first()
    context = {
        'contact_form': contact_form,
        'site_setting': site_setting
    }

    return render(request, 'contact_us.html', context)
