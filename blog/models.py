from django.db import models
from django.utils.html import format_html
from django.conf import settings
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField
import readtime
import math

# Create your models here.
# Category Model


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=100)
    cat_description = models.TextField()
    cat_url = models.CharField(max_length=100)
    cat_image = models.ImageField(upload_to='category/')
    cat_add_date = models.DateTimeField(auto_now_add=True, null=True)

    def show_cat_image(self):
        return format_html('<img src="/media/{}" style="width:40px; heigth:40px;" /> '.format(self.cat_image))

    def __str__(self):
        return self.cat_title


# Post Model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=100)
    post_content = HTMLField()
    post_url = models.CharField(max_length=100)
    post_in_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = TaggableManager()
    post_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    post_image = models.ImageField(upload_to='post/')

    def __str__(self):
        return self.post_title

    def datepublished(self):
        return self.published_date.strftime('%B %d %Y')

    def get_readtime(self):
        result = readtime.of_text(self.post_content)
        return result.text

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.published_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


class HeaderMenu(models.Model):
    menu_item = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='menu_item', blank=True, null=True)

    def __str__(self):
        return str(self.menu_item)

    class Meta:
        verbose_name = "Header Menu item"
        verbose_name_plural = "header Menu"
        db_table = "headermenu"


class HeaderDropdownMenu(models.Model):
    header_drop_menu_item = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='header_drop_menu_item', blank=True, null=True)

    def __str__(self):
        return str(self.header_drop_menu_item)

    class Meta:
        verbose_name = "Header Dropdown Menu item"
        verbose_name_plural = "header Dropdown Menu"
        db_table = "headerdropdownmenu"


class SocialSetting(models.Model):
    youtube_link = models.URLField(blank=True, null=True)
    fcebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Social Setting"
        verbose_name_plural = "Social Settings"
        db_table = "socialsettings"
    socialLinkName = 'Social Links'

    def __str__(self):
        return self.socialLinkName


class SiteDetail(models.Model):
    site_name = models.CharField(max_length=255)
    site_description = models.CharField(max_length=255)
    site_logo = models.ImageField(upload_to='logo/')
    favicon = models.ImageField(upload_to='logo/')

    def __unicode__(self):
        return self.site_name

    def __str__(self):
        return self.site_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, default="Dhaka, bangladesh")
    user_bio = models.TextField(blank=True, default="Creative")
    author_url = models.URLField(blank=True, null=True, default="https://webdeck99.blogspot.com/")
    author_fcebook_link = models.URLField(blank=True, null=True ,default="https://www.facebook.com/ronytarafder99")
    user_image = models.ImageField(upload_to='user/', default='user/avatardefault.png')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
