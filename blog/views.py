from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Tag, Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import PostForm, CommentForm
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def post_list(request):
    CategoryQ = request.GET.get('category') # by default all
    TagQ = request.GET.getlist('tag') # getlist will return a list and store in TagQ
    SearchQ = request.GET.get('q')
    
    posts = Post.objects.all()

    if CategoryQ: # if any category query occurs
        posts = posts.filter(category__name=CategoryQ) # filter the post
        
    if TagQ:
        posts = posts.filter(tag__name__in=TagQ).distinct()
        
    if SearchQ:
        posts = posts.filter(Q(title__icontains = SearchQ)|
                             Q(content__icontains = SearchQ)|
                             Q(tag__name__icontains = SearchQ)|
                             Q(category__name__icontains = SearchQ) 
                             ).distinct()
    
    # Paginator
    paginator = Paginator(posts, 3) # per page will keep 3 posts
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    
    contexts = {
        'page_obj': page_obj,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'search_query': SearchQ,
        'tag_query': TagQ,
        'category_query': CategoryQ,
    }
    return render(request, '', context=contexts)
        