from django.urls import path

# from articleapp.veiws import ArticleCreateView
from . import views


     
app_name = 'article'
urlpatterns = [
    path("base/",views.BaseArticle.as_view(),name="article_class_base"),
    path("basel/",views.BaseArticleList.as_view(),name="article_base_list"),
    path("",views.base_article,name="home"),
    
    path("create/",views.ArticleCreateView.as_view(),name="article_create"),
    path("list/",views.ArticleListView.as_view(),name="article_list"),
    
    path("detail/<int:pk>/",views.ArticleDetailView.as_view(),name="article_detail"),
    # path("detail/<int:id>/",views.ArticleDetailView.as_view(),name="article-detail"),

    path("update/<int:pk>/",views.ArticleUpdateView.as_view(),name="article-update"),
    path("delete/<int:pk>/",views.ArticleDeleteView.as_view(),name="article-delete")
] 
