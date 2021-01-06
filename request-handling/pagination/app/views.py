import csv


from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlencode


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    list_item_bus_stations = []

    with open(settings.BUS_STATION_CSV, encoding='cp1251') as f:
        reader = csv.DictReader(f)
        for dict_bus_stations in reader:
            list_item_bus_stations.append(
                {'Name': dict_bus_stations['Name'], 'Street': dict_bus_stations['Street'],
                 'District': dict_bus_stations['District']})

    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(list_item_bus_stations, settings.ITEMS_PAGE)
    page_obj = paginator.get_page(current_page)
    curr_page = page_obj.object_list

    if page_obj.has_next():
        params = {'page': page_obj.next_page_number()}
        next_page_url = '?'.join((reverse('bus_stations'), urlencode(params)))
    else:
        next_page_url = None

    if page_obj.has_previous():
        params_prev = {'page': page_obj.previous_page_number()}
        prev_page_url = '?'.join((reverse('bus_stations'), urlencode(params_prev)))
    else:
        prev_page_url = None

    context = {
        'bus_stations': curr_page,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }

    return render(request, 'index.html', context=context)
