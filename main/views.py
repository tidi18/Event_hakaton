from django.shortcuts import render
# from register.models import Team, Member, Hakaton


def index(request):
    return render(request, "main/index.html")