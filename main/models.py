from django.db import models


class Hakaton(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование', blank=False, null=True)
    date = models.DateField(blank=False, verbose_name='Дата (-ы) проведения', null=True)
    rules = models.TextField(blank=False, verbose_name='Правила сорвнования', null=True)
    anons = models.TextField(blank=False, verbose_name='Краткий анонс', null=True)
    prizes = models.TextField(blank=False, verbose_name='Призы', null=True)
    contact = models.CharField(max_length=255,  blank=False, verbose_name='Контакты', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Хакатон'
        verbose_name_plural = 'Хакатоны'




