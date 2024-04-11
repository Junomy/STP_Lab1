# Generated by Django 4.2.11 on 2024-04-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_category_slug_alter_article_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія для публікації’', 'verbose_name_plural': 'Категорії для публікації’'},
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique_for_date='pub_date', verbose_name='Слаг'),
        ),
    ]