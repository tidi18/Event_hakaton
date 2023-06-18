from django.shortcuts import render
from .models import Hakaton
from register.models import Team, Member


def index(request):
    list_hakaton = Hakaton.objects.all()
    list_team = Team.objects.all()
    lsit_member = Member.objects.all()
    return render(request, "main/index.html", {'list_hakaton': list_hakaton, 'list_team': list_team, 'list_member': lsit_member})