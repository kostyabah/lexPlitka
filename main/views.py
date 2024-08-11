from django.shortcuts import render
from gallery.models import imggal
from news.models import Product, Category, Master, Service, SinkFromTile
import random

def index(request):
    return render(request, 'main/index.html')


def products(request):
    
    
    # for prod in productsList:
    #     print(prod.id)
    productsList = list(Product.objects.all());
    return render(request, 'main/products.html',{'products': productsList})

def services(request):
    
    
    serviceList = list(Service.objects.all());
    return render(request, 'main/services.html',{'services': serviceList})

def masters (request):
    
    masterList = list(Master.objects.all());
    return render(request, 'main/masters.html', {'masters': masterList})

def gallery(request):
    return render(request, 'gallery/gallery.html')



def about(request):
    return render(request, 'main/about.html')



def contacts(request):
    return render(request, 'button/contacts.html')

def imagedisplay(request):
    resultsdisplay=list(imggal.objects.all())
    resultsdisplay=random.sample(resultsdisplay, 16)
    return render(request, 'gallery/gallery.html',{'imggal':resultsdisplay})