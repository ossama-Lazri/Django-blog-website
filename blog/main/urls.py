from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('all_blogs/', views.all_blogs, name='all_blogs'),
    path('single_blog/', views.single_blog, name='single_blog'),
]