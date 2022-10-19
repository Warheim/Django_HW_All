# Generated by Django 4.1.2 on 2022-10-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_tag_options_rename_title_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной тэг'),
        ),
        migrations.AddField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(related_name='tags', through='articles.Scope', to='articles.article'),
        ),
    ]
