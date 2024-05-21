from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
import json
from . import utils

from accounts.utils import get_popular_stocks, get_gaining_and_losing_stocks, get_stock_data

from accounts.models import User


def index(request):  # anasayfa

    context = {}

    popular_stocks = get_popular_stocks()
    gaining_stocks, losing_stocks = get_gaining_and_losing_stocks()

    context["graph_data"] = json.dumps(get_stock_data("XU100.IS"))
    context["popular_stocks"] = popular_stocks
    context["gaining_stocks"] = gaining_stocks
    context["losing_stocks"] = losing_stocks
    
    return render(request, "index.html", context)

import json
def stock_data(request):
    context = {}
    symbol = request.GET.get("symbol")
    print(symbol)
    data_to_return = get_stock_data(symbol)
    print(data_to_return)
    context["stock_data"] = json.dumps(data_to_return)
    context["SYMBOL"] = json.dumps(symbol)
    return render(request, "stock.html", context)


def all_stocks(request):  #stock degerleri
    context = {}

    return render(request, "stocks.html", context)


    

def about(request): #hakkımızda 
    context= {
        'page_title': 'About Us',
        'content': 'This is the about page.'
    }
    return render (request,"about.html",context)

def contact(request): #iletişim
    context ={}
    return render(request,"contact.html",context)

    """"
    web serveri icin gerekli endpointler:
    genel:
    landing
    dashboard  (takip listesi)
    hakkinda
    iletisim
    
    kullanici ile alakali:
    giriş
    kayit olma
    sahip olduğu hisseleri ve para miktarini göreceği sayfa(portfoy sayfasi)

    tema(borsa) ile ilgili şeyler: 
    tüm hisselerin görüleceği yer 
    tek bir hissenin detaylarinin görüleceği bir yer
    alim satim ve teknik analizin yapilacaği sayfa yada pop-up
    """