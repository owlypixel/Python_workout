"""electronic_kit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from products.views import list_products, CategoriesList, ProductDetail, CategoryDetail, ProductViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', list_products, name='products'),
    url(r'^categories/$', CategoriesList.as_view(), name='categories'),
    url(r'^products/(?P<pk>[-\w]+)/$', ProductDetail.as_view(), name='product-detail'),
    url(r'^categories/(?P<pk>[-\w]+)/$', CategoryDetail.as_view(), name='category-detail'),
    url(r'^api/', include('products.urls', namespace='core')),
]  

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
