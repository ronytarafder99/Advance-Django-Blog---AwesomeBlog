from django.contrib import admin
from .models import aboutPage, contactPage, privacyPage

# Register your models here.
admin.site.register(aboutPage)
admin.site.register(contactPage)
admin.site.register(privacyPage)