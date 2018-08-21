from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.get_search_field, name='get_search_field'),
    path('', views.index, name='index'),
]