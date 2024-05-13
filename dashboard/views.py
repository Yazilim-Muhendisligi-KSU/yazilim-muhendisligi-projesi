from django.shortcuts import render

from django.http import JsonResponse, HttpResponse

from . import utils

from accounts.models import User


def index(request):  # anasayfa

    context = {}
    
    return render(request, "index.html", context)


def all_stocks(request):
    context = {}

    return render(request, "index.html", context)
    



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