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
    try:
        books = Book.objects.filter(pub_date=pub_date)
        if books:
            template = 'books/books_list.html'
            context = {'books': books}
            return render(request, template, context)
        else:
            return HttpResponse('<h3>No books for such a date</h3>')
    except ValidationError:
        return HttpResponse(
            f'<h3>"{pub_date}" is incorrect format for date. Please type date in YYYY-MM-DD format.</h3>')
