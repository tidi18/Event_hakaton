from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import re
from pytils.translit import slugify


def validate_telegram(value):
    # Проверка, что значение соответствует формату Telegram (начинается с @ и содержит только буквы, цифры и _)
    if not re.match(r'^@[\w\d_]+$', value):
        raise ValidationError('Неверный формат Telegram. Имя пользователя должно начинаться с @ и содержать только буквы, цифры и _.')


class Hakaton(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование', blank=False, null=True)
    date = models.DateField(blank=False, verbose_name='Дата (-ы) проведения', null=True)
    rules = models.TextField(blank=False, verbose_name='Правила сорвнования', null=True)
    anons = models.TextField(blank=False, verbose_name='Краткий анонс', null=True)
    prizes = models.TextField(blank=False, verbose_name='Призы', null=True)
    telegram = models.CharField(max_length=255,  blank=False, verbose_name='Telegram', null=True, validators=[validate_telegram])
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Hakaton, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Хакатон'
        verbose_name_plural = 'Хакатоны'


class Team(models.Model):
    hakaton = models.ForeignKey(Hakaton,  related_name='teams', verbose_name='Хакатон', on_delete=models.CASCADE)
    name_team = models.CharField(max_length=255, blank=False, verbose_name='Название команды', unique=True)
    max_members = models.IntegerField(verbose_name='Количество участников команды',
    validators=[
             MinValueValidator(0, message='Значение должно быть больше или равно 0'),
             MaxValueValidator(4, message='Значение должно быть меньше или равно 4'),
        ]
    )

    def __str__(self):
        return f'{self.name_team} ({self.hakaton})'

    def is_full(self):
        return self.members.count() >= self.max_members

    class Meta:
        verbose_name = 'Команду'
        verbose_name_plural = 'Команды'


class Member(models.Model):
    team = models.ForeignKey(Team, related_name='members', verbose_name='Команда', on_delete=models.CASCADE)
    is_captain = models.BooleanField(verbose_name='Капитан команды', default=False)
    name = models.CharField(max_length=50, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=100, blank=False, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст',
        validators=[
            MinValueValidator(11, message='Возраст должен быть больше или равен 11'),
            MaxValueValidator(17, message='Возраст должен быть меньше или равен 17')
        ]
    )

    def __str__(self):
        return f'{self.team} {self.name}'

    class Meta:
        verbose_name = 'Участника'
        verbose_name_plural = 'Участники'








