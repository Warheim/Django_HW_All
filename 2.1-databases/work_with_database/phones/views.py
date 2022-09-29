from django.shortcuts import render, redirect
from phones.management.commands.import_phones import Command
from phones.models import Phone
import csv


def index(request):
    with open('phones.csv', 'r', encoding='UTF-8') as file:
        phones = list(csv.DictReader(file, delimiter=';'))
    for phone in phones:
        create_phone = Phone(id=phone['id'], name=phone['name'], image=phone['image'], price=phone['price'],
                             release_date=phone['release_date'], lte_exists=phone['lte_exists'])
        create_phone.save()
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
