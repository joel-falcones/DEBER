from django.urls import path
from prueba import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('sample/', views.sample, name='sample'),
    path('store/', views.store, name='store'),
]