from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        chosen_few = []
        for form in self.forms:
            tag = form.cleaned_data.get('tag')
            if tag not in chosen_few:
                chosen_few.append(tag)
            else:
                chosen_few = []
                raise ValidationError('Выберите разные тэги')
            if form.cleaned_data.get('is_main'):
                counter += 1
        if counter == 0:
            raise ValidationError('Выберите один основной тэг')
        elif counter > 1:
            raise ValidationError('Основной тэг может быть только один')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
