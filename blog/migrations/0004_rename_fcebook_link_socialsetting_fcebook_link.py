# Generated by Django 3.2.7 on 2021-09-16 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210913_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialsetting',
            old_name='Fcebook_link',
            new_name='fcebook_link',
        ),
    ]
