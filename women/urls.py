from django.urls import path
from . import views

app_name = 'women'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('categories/', views.categories, name='categories'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact, name='contact'),
]