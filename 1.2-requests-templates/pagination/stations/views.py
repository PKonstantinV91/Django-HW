from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


list_ = []

with open(r'C:\Нетология\Django\Материалы\dj-homeworks\1.2-requests-templates\pagination\data-398-2018-08-30.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for el in reader:
        list_.append(el)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(list_, 10)
    pag = paginator.get_page(page_num)

    context = {
        'bus_stations': pag,
        'page': pag,
    }
    
    return render(request, 'stations/index.html', context)
