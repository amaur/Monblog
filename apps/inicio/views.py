from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView,CreateView,ListView
from django.http import HttpResponse
from django.template import RequestContext,loader
from apps.artigos.models import Article
from apps.categos.models import Categorie

# Create your views here.

def Index(request):
    
    categos = Categorie.objects.all()
    artigos =Article.objects.all()
    context = {
        'categorias': categos,
        'article': artigos
    }
    return render(request, 'inicio/index.html', context)
    
def my_page(request):
    categos = Categorie.objects.all()
    context = {
        'categorias': categos}
    return render(request,'inicio/Zinli.html',context)
   

def art_likes(request):
    context = RequestContext(request)
    art_id = None
    if request.method == 'GET':
        art_id = request.GET['article_id']

    likes = 0
    if art_id:
        article = Article.objects.get(id=int(art_id))
        if article:
            likes = article.likes + 1
            article.likes =  likes
            article.save()

    return HttpResponse(likes)


