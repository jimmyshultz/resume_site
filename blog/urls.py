"""Defines URL patterns for blog."""

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    #Blog home page
    path('', views.blog_homepage, name='blog'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('<int:blogpost_id>/', views.blogpost, name='blogpost'),
    path('new_comment/<int:blogpost_id>/', views.new_comment, name='new_comment'),
]