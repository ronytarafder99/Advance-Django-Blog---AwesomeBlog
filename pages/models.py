from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class aboutPage(models.Model):
    About_page_id = models.AutoField(primary_key=True)
    About_page_title = models.CharField(max_length=100)
    About_page_content = HTMLField()

class contactPage(models.Model):
    contact_page_id = models.AutoField(primary_key=True)
    contact_page_title = models.CharField(max_length=100)
    contact_page_content = HTMLField()

class privacyPage(models.Model):
    privacy_page_id = models.AutoField(primary_key=True)
    privacy_page_title = models.CharField(max_length=100)
    privacy_page_content = HTMLField()