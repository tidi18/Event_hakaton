# Generated by Django 4.2.1 on 2023-05-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_info_hakaton_alter_hakaton_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='hakaton',
            name='anons',
            field=models.TextField(null=True, verbose_name='Краткий анонс'),
        ),
        migrations.AddField(
            model_name='hakaton',
            name='prizes',
            field=models.TextField(null=True, verbose_name='Призы'),
        ),
        migrations.AlterField(
            model_name='hakaton',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата (-ы) проведения'),
        ),
        migrations.AlterField(
            model_name='hakaton',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='hakaton',
            name='rules',
            field=models.TextField(null=True, verbose_name='Правила сорвнования'),
        ),
    ]
