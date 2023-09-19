from django.urls import path
from . import views

urlpatterns = [
    path('register_team/', views.RegisterTeamView.as_view(), name='register_team'),
    path('register_member/', views.RegisterMembersView.as_view(), name='register_member')


]
