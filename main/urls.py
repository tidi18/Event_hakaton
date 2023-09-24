from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/about', views.about, name='about'),
    path('main/hakaton/<slug:slug>', views.HakatonDetailView.as_view(), name='hakaton_detail'),
]
