from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home/$', views.homepage, name='home'),
    url(r'^greet/(\w+)/$', views.greet, name='greet'),
]