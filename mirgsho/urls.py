"""mirgsho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from main import views as MainViews
admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),    
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^roxyfileman/', include('roxyfileman.urls')),
    path('', MainViews.IndexView, name='index'),
    url(r'^contacts/', MainViews.ContactsView, name='contacts'),
    #url(r'^catalog/', MainViews.CatalogView, name='catalog'),
    url(r'^(?P<category>[\w-]+)$', MainViews.CatalogView, name='catalog'),
    url(r'^(?P<category>[\w-]+)/(?P<subcategory>[\w-]+)/$', MainViews.CatalogView_detail, name='catalog_detail'),
    url(r'^(?P<category>[\w-]+)/(?P<subcategory>[\w-]+)/(?P<product_slug>[\w-]+)$', MainViews.ProductView, name='product'),
    url(r'^news/(?P<slug>[\w-]+)$', MainViews.NewsView_detail, name='news_detail'),
    url(r'^news/', MainViews.NewsView, name='news'),    
]
