# Generated by Django 3.2.7 on 2021-09-16 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_contactpage_privacypage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='About_page_image',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='contact_page_image',
        ),
        migrations.RemoveField(
            model_name='privacypage',
            name='privacy_page_image',
        ),
    ]
