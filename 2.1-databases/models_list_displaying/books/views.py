from django.core.exceptions import ValidationError
from django.shortcuts import render
from .models import Book
from django.http import HttpResponse


def books_view(request):
    books = Book.objects.all().order_by('pub_date')
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)


def books_for_date(request, pub_date):
    template = 'books/books_list.html'
    books_obj = Book.objects.filter(pub_date=pub_date)
    books_next = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    books_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    context = {
        'books': books_obj,
        'next_book': books_next,
        'prev_book': books_previous,
    }
    return render(request, context, template)
