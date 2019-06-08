from django.shortcuts import render

from .models import Mineral

# Create your views here.


def home_page(request):
    # import all items from database
    minerals = Mineral.objects.all()

    # load items to view
    return render(request, 'website/home_page.html', {'minerals': minerals})


def mineral_detail(request, mineral_pk):
    return render(request, 'website/detail.html', {'mineral': {}})