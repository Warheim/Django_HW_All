from django.core.management import BaseCommand

from articles.models import Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        tags = ['Политика', 'Наука', 'Культура', 'Спорт', 'Здоровье', 'Мир', 'Страна', 'Город']
        for tag in tags:
            Tag.objects.create(title=tag)
