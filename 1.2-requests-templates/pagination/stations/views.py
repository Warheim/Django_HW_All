from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, encoding='UTF-8') as work:
        reader = csv.DictReader(work)
        bus_stations_list = [station for station in reader]
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(bus_stations_list, 10)
        page = paginator.get_page(page_number)
        context = {
            'page': page,
            'bus_stations': page.object_list,
        }
        return render(request, 'stations/index.html', context)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
