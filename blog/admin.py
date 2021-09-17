from django.contrib import admin
from .models import Category, Post, HeaderMenu, SocialSetting, SiteDetail, HeaderDropdownMenu
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('show_cat_image', 'cat_title',
                    'cat_description', 'cat_url', 'cat_add_date')
    search_fields = ('cat_title', 'cat_id',)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)
admin.site.register(HeaderMenu)
admin.site.register(SocialSetting)
admin.site.register(SiteDetail)
admin.site.register(HeaderDropdownMenu)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
