from django.shortcuts import render

from django.http import JsonResponse, HttpResponse

from . import utils

from accounts.models import User


def index(request):  # anasayfa

    context = {}
    
    return render(request, "index.html", context)


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