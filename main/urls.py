from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name=''),
    path('create', views.create, name='create'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('debug', views.get_exсeption, name='debug'),
]
