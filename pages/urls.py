from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import AboutPageView, ContactPageView, PrivacyPageView

app_name = "pages"

urlpatterns = [
    path('about', AboutPageView, name='about'),
    path('contact', ContactPageView, name='contact'),
    path('privacy', PrivacyPageView, name='privacy'),
]
