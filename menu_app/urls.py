from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-page'),
    path('1/', views.view_2, name='page-2'),
    path('2/', views.view_3, name='page-3'),
    path('3/', views.view_4, name='page-4'),
    path('4/', views.view_5, name='page-5'),
    path('5/', views.view_6, name='page-6'),
]