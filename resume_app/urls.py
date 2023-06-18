from django.urls import path
from . import views

app_name = 'resume_app'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]