from django.shortcuts import render
from articles.models import Article
from articles.admin import ScopeInlineFormset


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, template, context)
