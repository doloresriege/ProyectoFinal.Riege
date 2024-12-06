from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('pages/', views.blog_list, name='blog-list'),
    path('pages/<int:page_id>/', views.blog_detail, name='blog-detail'),
]