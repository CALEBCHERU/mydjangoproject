"""
URL configuration for mydjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path,include

from pages import views
from products import views as v
from products.views import ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #The below code is most prefered metoh to add urls
    path("",include("myapp.urls")),
    
    #Pages app
    path("",views.home_view, name='home'),
    path("contact/",views.contact),
    path("theband/",views.html),
    path("base/",views.base),
    path("contact1/",views.base1),
    
    # //product app
    path("product/",v.baseProduct, ),
    path("product/form/",v.RawProduct_v),
     #access the database
    path('productdetail/<int:my_id>/',v.dynamic_lookup),
    #classView
    path("productdetail/all",ProductListView.as_view()),
    
    #article app
    path("article/",include("articleapp.urls")),
    
    #room/freecode
    path("",include("freecodeapp.urls")),
    
    path('api-auth/', include('rest_framework.urls')),
    
    path('', include('api.urls')),
    
    path('', include('calebform.urls'))
    
]
