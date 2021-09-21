from django.contrib.auth.models import User
from django.shortcuts import render
from blog.models import Post, Category, HeaderMenu, SocialSetting, HeaderDropdownMenu, SiteDetail, Profile
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.views.generic import TemplateView
from django.db.models import Q

# Create your views here.


def home(request):
    # load the posts from database
    posts_list = Post.objects.all().order_by('-created_date')
    latest_post = Post.objects.order_by('?')[:5]
    header_post = Post.objects.order_by('-created_date')[:4]

    cats = Category.objects.all()
    tags = Tag.objects.all()

    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')

    socialLink = SocialSetting.objects.filter().first()
    menuItem = HeaderMenu.objects.all()
    headerDropdownMenu = HeaderDropdownMenu.objects.all()
    siteDetail = SiteDetail.objects.filter().first()

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    home_data = {
        'posts': posts,
        'page': page,
        'latest_post': latest_post,
        'header_post': header_post,
        'cats': cats,
        'tags': tags,
        'menuItem': menuItem,
        'headerDropdownMenu': headerDropdownMenu,
        'siteDetail': siteDetail,
        'socialLink': socialLink,
    }

    return render(request, 'home.html', home_data,)


def post(request, url):
    header_post = Post.objects.order_by('-created_date')[:4]
    tags = Tag.objects.all()
    siteDetail = SiteDetail.objects.filter().first()
    socialLink = SocialSetting.objects.filter().first()
    post = Post.objects.get(post_url=url)
    cat = post.post_in_cat
    cats = Category.objects.all()
    menuItem = HeaderMenu.objects.all()
    headerDropdownMenu = HeaderDropdownMenu.objects.all()
    related_posts = Post.objects.filter(post_in_cat=cat)[:3]
    post_data = {
        'post': post,
        'cats': cats,
        'cat': cat,
        'menuItem': menuItem,
        'headerDropdownMenu': headerDropdownMenu,
        'siteDetail': siteDetail,
        'related_posts': related_posts,
        'socialLink': socialLink,
        'header_post': header_post,
        'tags': tags,
    }

    return render(request, 'posts.html', post_data)


def category(request, url):
    cats = Category.objects.all()
    cat = Category.objects.get(cat_url=url)
    tags = Tag.objects.all()
    header_post = Post.objects.order_by('-created_date')[:4]
    posts_list = Post.objects.filter(post_in_cat=cat)
    paginator = Paginator(posts_list, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    menuItem = HeaderMenu.objects.all()
    headerDropdownMenu = HeaderDropdownMenu.objects.all()
    siteDetail = SiteDetail.objects.filter().first()
    socialLink = SocialSetting.objects.filter().first()
    category_data = {
        'posts': posts,
        'cats': cats,
        'cat': cat,
        'menuItem': menuItem,
        'siteDetail': siteDetail,
        'socialLink': socialLink,
        'headerDropdownMenu': headerDropdownMenu,
        'num_post': posts_list.count(),
        'tags': tags,
        'header_post': header_post,
    }

    return render(request, "category.html", category_data)


def FilterByTag(request, tag):
    header_post = Post.objects.order_by('-created_date')[:4]
    tags = Tag.objects.all()
    tag = Tag.objects.get(name=tag)
    cats = Category.objects.all()
    siteDetail = SiteDetail.objects.filter().first()
    socialLink = SocialSetting.objects.filter().first()
    headerDropdownMenu = HeaderDropdownMenu.objects.all()
    posts_list = Post.objects.filter(
        tags__name__in=[tag]).order_by('-created_date')
    paginator = Paginator(posts_list, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    menuItem = HeaderMenu.objects.all()
    category_data = {
        'tag_num_posts': posts_list.count(),
        'posts': posts,
        'cats': cats,
        'menuItem': menuItem,
        'header_post': header_post,
        'tags': tags,
        'tag': tag,
        'siteDetail': siteDetail,
        'headerDropdownMenu': headerDropdownMenu,
        'socialLink': socialLink,
    }
    return render(request, "tag.html", category_data)


def authorView(request, username, author_id):
    header_post = Post.objects.order_by('-created_date')[:4]
    tags = Tag.objects.all()
    socialLink = SocialSetting.objects.filter().first()
    menuItem = HeaderMenu.objects.all()
    headerDropdownMenu = HeaderDropdownMenu.objects.all()
    siteDetail = SiteDetail.objects.filter().first()

    posts_list = Post.objects.filter(post_user=author_id)
    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')

    try:
        author_post = paginator.page(page)
    except PageNotAnInteger:
        author_post = paginator.page(1)
    except EmptyPage:
        author_post = paginator.page(paginator.num_pages)
    profile = Profile.objects.filter(user=author_id).first()
    currentUser = User.objects.filter(username=username).first()
    author_data = {
        'menuItem': menuItem,
        'headerDropdownMenu': headerDropdownMenu,
        'siteDetail': siteDetail,
        'socialLink': socialLink,
        'author_post': author_post,
        'header_post': header_post,
        'profile': profile,
        'tags': tags,
        'currentUser': currentUser,
        'num_post': posts_list.count(),
    }
    return render(request, "author.html", author_data)


def SearchResultsView(request):
    header_post = Post.objects.order_by('-created_date')[:4]
    tags = Tag.objects.all()
    socialLink = SocialSetting.objects.filter().first()
    menuItem = HeaderMenu.objects.all()
    headerDropdownMenu = HeaderDropdownMenu.objects.all()
    siteDetail = SiteDetail.objects.filter().first()
    query = request.GET.get('q')

    posts_list = Post.objects.filter(
        Q(post_title__icontains=query) | Q(post_content__icontains=query)
    )
    paginator = Paginator(posts_list, 100)
    page = request.GET.get('page')

    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    search_data = {
        'object_list_count': posts_list.count(),
        'object_list': object_list,
        'query': query,
        'socialLink': socialLink,
        'menuItem': menuItem,
        'headerDropdownMenu': headerDropdownMenu,
        'siteDetail': siteDetail,
        'header_post': header_post,
        'tags': tags,
    }
    return render(request, 'search_results.html', search_data)
