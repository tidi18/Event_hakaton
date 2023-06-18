# Generated by Django 4.2.1 on 2023-05-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_team', models.CharField(max_length=255, verbose_name='Команда')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('age', models.CharField(max_length=2, verbose_name='Возраст')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_team', models.CharField(max_length=255, verbose_name='Название команды')),
                ('name', models.CharField(max_length=50, verbose_name='Имя капитана')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия капитана')),
                ('age', models.CharField(max_length=2, verbose_name='Возраст капитана')),
                ('phone', models.CharField(blank=True, max_length=13, verbose_name='Номер телефона')),
                ('number_member', models.CharField(max_length=1, verbose_name='Количества участников в команде')),
            ],
        ),
    ]