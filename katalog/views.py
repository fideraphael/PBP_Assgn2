from django.shortcuts import render
from katalog.models import CatalogItem


def show_catalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
        'list_item': data_katalog_item,
        'name': 'Raphael',
        'StudentID':'2106720986'
    }
    return render(request, "katalog.html", context)
# TODO: Create your views here.
