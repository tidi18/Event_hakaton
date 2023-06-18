from django.urls import path
from .views import RegisterTeamView, RegisterMembersView


urlpatterns = [
    path('register_team/', RegisterTeamView.as_view(), name='register_team'),
    path('register-members/', RegisterMembersView.as_view(), name='register_members'),

]
