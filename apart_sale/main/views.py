from django.shortcuts import render

from apartments.models import Apartments


def index(request):
    favorite_apartments = Apartments.objects.filter(favorite=True, status='for_sale', show=True)
    last_apartments = Apartments.objects.order_by('-id')[:4]
    if len(favorite_apartments) == 0:
        favorite_apartments = Apartments.objects.filter(status='for_sale', show=True)[:3]

    data = {
        'favorite_apartments': favorite_apartments,
        'last_apartments': last_apartments,
    }

    return render(request, "index.html", context=data)
