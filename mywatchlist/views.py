from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchListItem


def show_watchlist(request):
    data_watchlist_item = WatchListItem.objects.all()
    context = {
        'list_item': data_watchlist_item,
        'name': 'Raphael',
        'StudentID':'2106720986'
    }
    return render(request, "watchlist.html", context)

def show_xml(request):
    data = WatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
