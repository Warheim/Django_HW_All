from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    response = request.GET.get('sort')
    if response == 'name':
        phones = Phone.objects.all().order_by('name')
    elif response == 'min_price':
        phones = Phone.objects.all().order_by('-price')
    elif response == 'max_price':
        phones = Phone.objects.all().order_by('price')
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
