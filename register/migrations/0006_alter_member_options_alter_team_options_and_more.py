# Generated by Django 4.2.1 on 2023-05-04 08:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_alter_team_max_members'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'Участника', 'verbose_name_plural': 'Участники'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Команду', 'verbose_name_plural': 'Команды'},
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(11, message='Age must be greater than or equal to 11'), django.core.validators.MaxValueValidator(17, message='Age must be less than or equal to 17')], verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_captain',
            field=models.BooleanField(default=False, verbose_name='Капитан команды'),
        ),
        migrations.AlterField(
            model_name='team',
            name='max_members',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Value must be greater than or equal to 0'), django.core.validators.MaxValueValidator(4, message='Value must be less than or equal to 4')], verbose_name='Количество участников команды'),
        ),
    ]