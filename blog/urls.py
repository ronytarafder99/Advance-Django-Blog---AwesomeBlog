from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, post, category, FilterByTag, authorView

app_name = "blog"

urlpatterns = [
    path('', home, name='home'),
    path('blog/<slug:url>',post),
    path('category/<slug:url>',category),
    path('tag/<slug:tag>/', FilterByTag, name='tag'),
    path('<str:username>/<str:author_id>', authorView),
]