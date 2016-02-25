#coding:utf-8
from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponse
from .models import Item

def show_next(request):
    itter = cache.get('item')
    print itter
    if itter >= 0:
        items = Item.objects.filter(item_processed=False)
        if not items:
            response = "В базі немає записів, або всі запити оброблені"
            return HttpResponse(response)
        nxt = items[itter+1:]
        if nxt:
            cache.set('item', itter+1, 3000)
        else:
            cache.set('item', 0, 3000)
        response = "Id: %s, name: %s"%(items[itter].id, items[itter].item_name )
        return HttpResponse(response)
    else:
        items = Item.objects.filter(item_processed=False)
        if items:
            cache.set('item', 1, 3000)
            response = "Id: %s, name: %s"%(items[0].id, items[0].item_name )
            return HttpResponse(response)
        else:
            response = "В базі немає записів, або всі запити оброблені"
            return HttpResponse(response)


def processed(request, id):
    chk_item = Item.objects.filter(id=id)
    if chk_item and request.GET.get('processed') and request.GET.get('processed') == 'true':
        chk_item.update(item_processed = True)
        return HttpResponse('status: 1')
    else:
        return HttpResponse('status: 0')
