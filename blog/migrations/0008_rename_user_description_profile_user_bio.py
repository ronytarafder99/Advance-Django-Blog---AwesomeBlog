# Generated by Django 3.2.7 on 2021-09-16 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210916_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_description',
            new_name='user_bio',
        ),
    ]
