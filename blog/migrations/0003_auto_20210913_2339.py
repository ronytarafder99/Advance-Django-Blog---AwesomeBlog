# Generated by Django 3.2.7 on 2021-09-13 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_submenuonheader'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderDropdownMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_drop_menu_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='header_drop_menu_item', to='blog.category')),
            ],
            options={
                'verbose_name': 'Header Dropdown Menu item',
                'verbose_name_plural': 'header Dropdown Menu',
                'db_table': 'headerdropdownmenu',
            },
        ),
        migrations.DeleteModel(
            name='SubMenuOnHeader',
        ),
    ]
