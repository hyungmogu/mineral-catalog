from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'website/home_page.html', {'minerals': []})


def mineral_detail(request, mineral_pk):
    return render(request, 'website/detail.html', {'mineral': {}})