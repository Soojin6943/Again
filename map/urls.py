from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.map, name='map'),
    path('bulk/', views.bulk_import, name='bulk'),
    path('<str:category>/', views.detail, name='detail')
]