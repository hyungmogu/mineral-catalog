from django.shortcuts import render


# Create your views here.
def home_page(request):
    print(request)
    return render(request, 'website/home_page.html', {'minerals': []})