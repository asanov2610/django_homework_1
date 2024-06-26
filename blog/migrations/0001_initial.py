# Generated by Django 5.0.2 on 2024-06-14 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('body', models.TextField(max_length=1000, verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('is_published', models.BooleanField(default=True, verbose_name='Признак публикации')),
                ('views_counter', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
        ),
    ]
