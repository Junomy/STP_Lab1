# Generated by Django 4.2.11 on 2024-04-11 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', verbose_name='Слаг'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='app_blog.category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='article',
            name='main_page',
            field=models.BooleanField(default=False, help_text='Показувати на головній сторінці', verbose_name='Головна'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', unique_for_date='pub_date', verbose_name='Слаг'),
        ),
    ]
