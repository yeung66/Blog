#coding:utf-8
from django.shortcuts import render
from article.models import Article
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    post = Article.objects.all()
    page = request.GET.get('page',1)

    paginator =Paginator(post, 3)
    try:
        post_ = paginator.page(page)
    except PageNotAnInteger:
        post_ = paginator.page(1)
    except EmptyPage:
        post_ = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'post_list':post_})

def post(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html', {'post':post})

def type(request, type):
    try:
        post = Article.objects.filter(tag=type)
    except Article.DoesNotExist:
        raise Http404
    page = request.GET.get('page',1)
    paginator = Paginator(post, 3)
    try:
        post_ = paginator.page(page)
    except PageNotAnInteger:
        post_ = paginator.page(1)
    except EmptyPage:
        post_ = paginator.page(paginator.num_pages)
    return render(request,'type.html',{'post':post_})

def checkType(request):
    types = Article.objects.all().values('tag')
    type_list = []
    title_list=[]
    for i in types:
        if i['tag'] not in type_list:
            type_list.append(i['tag'])
    for j in type_list:
        title_list.append ( Article.objects.filter(tag=j))
    return render(request, 'type_list.html',{'tags':type_list,'title_list':title_list})

def about(request):
    return render(request,'about.html')