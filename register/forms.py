from django import forms
from captcha.fields import CaptchaField
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Team, Member


class TeamForm(forms.ModelForm):
    hakaton = forms.Select(attrs={'class': 'form-control'})
    name_team = forms.CharField(label='Название команды', widget=forms.TextInput(attrs={'class': 'form-input'}))
    max_members = forms.IntegerField(label='Количество участников', validators=[MinValueValidator(0, message='Значение должно быть больше или равно 0'), MaxValueValidator(4, message='Значение должно быть меньше или равно 4')])
    captcha = CaptchaField()

    class Meta:
        model = Team
        fields = ['hakaton', 'name_team', 'max_members', 'captcha']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['hakaton'].widget.attrs['placeholder'] = 'Укажите хакатон'
            self.fields['name_team'].widget.attrs['placeholder'] = ' Придумайте название команды'
            self.fields['max_members'].widget.attrs['placeholder'] = 'Укажите количество участников в команде'
            self.fields['captcha'].widget.attrs.update({"placeholder": 'Напишите текст с картинки'})
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "on"})


class MemberForm(forms.ModelForm):
    team = forms.Select(attrs={'class': 'form-control'})
    is_captain = forms.BooleanField(
        label='Капитан команды',
        widget=forms.CheckboxInput(attrs={'id': 'checkbox-control'}),
        required=False,
    )
    name = forms.CharField(label='Имя', max_length=50, widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    age = forms.IntegerField(label='Возраст',
        validators=[
            MinValueValidator(11, message='Возраст должен быть больше или равен 11'),
            MaxValueValidator(17, message='Возраст должен быть меньше или равен 17')
        ]
    )
    captcha = CaptchaField()

    class Meta:
        model = Member
        fields = ['team', 'is_captain', 'name', 'last_name', 'age', 'captcha']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'team':
                field.widget.attrs['placeholder'] = 'Укажите команду'
            elif field_name == 'name':
                field.widget.attrs['placeholder'] = 'Введите имя'
            elif field_name == 'last_name':
                field.widget.attrs['placeholder'] = 'Введите фамилию'
            elif field_name == 'age':
                field.widget.attrs['placeholder'] = 'Укажите ваш возраст'
            elif field_name == 'captcha':
                field.widget.attrs.update({"placeholder": 'Напишите текст с картинки'})

            field.widget.attrs.update({"class": "form-control", "autocomplete": "on"})

        # Отдельное применение класса для поля is_captain
        self.fields['is_captain'].widget.attrs['class'] = 'form-check-input checkbox-control'

