from django.shortcuts import render, redirect
from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    books = Book.objects.all().order_by('pub_date')
    template = 'books/books_list.html'
    context = {
        'books': books,
    }
    return render(request, template, context)


def books_for_date(request, pub_date):
    book = Book.objects.filter(pub_date=pub_date).first()
    next_book = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    prev_book = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    template = 'books/books_date.html'
    context = {
        'book': book,
        'next_book': next_book,
        'prev_book': prev_book,
    }
    return render(request, template, context)