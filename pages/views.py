from django.shortcuts import render
from pages.models import aboutPage, contactPage, privacyPage
# Create your views here.


def AboutPageView(request):
    about_Page = aboutPage.objects.filter().first()
    aboutData = {
        'about_Page': about_Page,
    }
    return render(request, 'pages/about.html', aboutData)


def ContactPageView(request):
    contact_Page = contactPage.objects.filter().first()
    contactData = {
        'contact_Page': contact_Page,
    }
    return render(request, 'pages/contact.html', contactData)


def PrivacyPageView(request):
    privacy_Page = privacyPage.objects.filter().first()
    privacyData = {
        'privacy_Page': privacy_Page,
    }
    return render(request, 'pages/privacy.html', privacyData)
