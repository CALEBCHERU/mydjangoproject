from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render,HttpResponse,get_object_or_404

from django.views.generic import (View,
    CreateView, ListView,DetailView,UpdateView,DeleteView)

from .models import ArticleModel

from .articleform import ArticleForm

from django.urls import reverse
# from django.utils.http import urlunquote
from urllib.parse import urlsplit, urlunsplit

#class based vie
class BaseArticle(View):
    def get(self,request):
        return render(request,"basearticle.html",{})

#function base vie
def base_article(request):
    return render(request,"basearticle.html",{})

class BaseArticleList(View):
    template_name = "article/BaseArticleList_list.html"
    queryset = ArticleModel.objects.all()
    
    def get(self,request):
        context ={'object_list': self.queryset}
        return render(request,self.template_name,context)
    

class ArticleCreateView(CreateView):
    template_name = "article/ArticleModel_create.html"   
                     #<article>/<modulename>_create.html
    form_class =  ArticleForm
    queryset = ArticleModel.objects.all()

    
    
    # the code below allow as to see hat as type and it gets printed on the terminal
    def clean_data(self,ArticleForm):
        print(ArticleForm.cleaned_data)
        return super().form_valid(ArticleForm)
    
    # this is used to render the same url . it just like refreshing but when u press the button save
    def get_success_url(self):
        current_url = self.request.get_full_path()
        # previous_url = self.get_previous_url(current_url)
        return  current_url

    # def get_previous_url(self, url):
    #     # Parse the URL into components
    #     scheme, netloc, path, query, fragment = urlsplit(url)
    #     # Split the path into segments and remove the last segment
    #     path_segments = path.rstrip('/').split('/')
    #     new_path = '/'.join(path_segments[:-1])
    #     # Reassemble the URL with the modified path
    #     previous_url = urlunsplit((scheme, netloc, new_path, query, fragment))
    #     return urlunquote(previous_url)
        
    
class ArticleListView(ListView):
    template_name = "article/ArticleModel_list.html"   
                     #<article>/<modulename>_list.html
    form_class =  ArticleForm
    queryset = ArticleModel.objects.all()
    
    def article_detail(self,request, pk):
        article = get_object_or_404(ArticleModel, pk=pk)
        return render(request, 'article_detail.html', {'article': article})
    
class ArticleDetailView(DetailView):
    template_name = "article/ArticleModel_detail.html"   
                     #<article>/<modulename>_detail.html
    form_class =  ArticleForm
    queryset = ArticleModel.objects.all()
    
    # def get_object(self):
    #     id_= self.kwargs.get("id")
    #     return get_object_or_404(ArticleModel, id=id_)
    #  get_object_or_404 >>this has to imported
        
    
class ArticleUpdateView(UpdateView):
    template_name = "article/ArticleModel_create.html"   
                     #<article>/<modulename>_create.html
    form_class =  ArticleForm
    queryset = ArticleModel.objects.all()
    
    
    
    def clean_data(self,ArticleForm):
        print(ArticleForm.cleaned_data)
        return super().form_valid(ArticleForm)
    
    
    def get_success_url(self):
        current_url = self.request.get_full_path()
        
        n = current_url.replace("/article/update/","")
        
        current_url = f"/article/detail/{n}"
        
        print(current_url)
        # previous_url = self.get_previous_url(current_url)
        return  current_url
    
    
class ArticleDeleteView(DeleteView):
    template_name = "article/ArticleModel_delete.html"   
                     #<article>/<modulename>_detail.html
    # form_class =  ArticleForm
    queryset = ArticleModel.objects.all()
    
    
    
    
    # success_url = "/article/list/"
    
    # the below code isjust the same as the upper commented code
    # i just rote it to illustrate how to use the reverse function. the reverse function must be imported
    def get_success_url(self):
        return reverse ('article:article-list')
    
    
    
