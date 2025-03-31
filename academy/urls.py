from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('yangiliklar/', views.news_list, name='news_list'),
    path('yangiliklar/<slug:slug>/', views.news_detail, name='news_detail'),
]