from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Apartments


def apartments(request, category_id='all'):
    all_category = ['for_sale', 'sales']

    if category_id in all_category:
        all_apartments = Apartments.objects.filter(status=category_id, show=True).order_by('-date')
    else:
        all_apartments = Apartments.objects.filter(show=True).order_by('-date')

    paginator = Paginator(all_apartments, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'all_apartments': all_apartments,
        'page_obj': page_obj,
        'category': category_id,
    }

    return render(request, 'apartments.html', context=data)


def single_apartment(request, apartment_id=0):
    apartment = Apartments.objects.get(id=apartment_id, show=True)

    if apartment:
        data = {
            'apartment': apartment,
        }

        return render(request, 'single_apartment.html', context=data)
