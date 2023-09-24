from django.shortcuts import render
from register.models import Team, Member, Hakaton
from django.views.generic import DetailView


def index(request):
    hakaton_data = Hakaton.objects.all()
    for hakaton in hakaton_data:
        # Удалить символ "@" из имени пользователя Telegram
        hakaton.telegram = hakaton.telegram[1:] if hakaton.telegram.startswith('@') else hakaton.telegram
    return render(request, "main/index.html", {'hakaton_data': hakaton_data})


def about(request):
    return render(request, 'main/about.html')


class HakatonDetailView(DetailView):
    model = Hakaton
    template_name = 'main/hakaton_detail.html'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Hakaton.objects.filter(slug=self.kwargs['slug'])
