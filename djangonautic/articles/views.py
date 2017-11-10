from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all().order_by('date');
    return render(request, 'articles/article_list.html', { 'articles': articles })

def article_detail(request, slug):
    return HttpResponse(slug)
