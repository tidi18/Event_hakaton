from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import TeamForm, MemberForm


class RegisterTeamView(CreateView):
    form_class = TeamForm
    success_url = reverse_lazy('register_member')
    template_name = "register/register_team.html"
    success_message = 'Команда создана'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация команды'
        return context


class RegisterMembersView(CreateView):
    form_class = MemberForm
    success_url = reverse_lazy('index')
    template_name = "register/register_members.html"
    success_message = 'Участник добавлен'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация участника команды'
        return context

    def form_valid(self, form):
        team = form.cleaned_data['team']

        existing_captain = team.members.filter(is_captain=True).first()
        if existing_captain and form.cleaned_data['is_captain']:
            form.add_error('is_captain', 'В этой команде уже есть капитан.')
            return self.form_invalid(form)

        if team.is_full():
            form.add_error(None, f'Команда {team} заполнена до максимального количества участников.')
            return self.form_invalid(form)

        return super().form_valid(form)
