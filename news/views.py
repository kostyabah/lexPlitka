from django.shortcuts import render
from .models import Articles, Product

# def news(request):
#     news = Articles.objects.order_by('-date')
#     return render(request, 'news/news.html', {'news': news})


def products(request):
    products = Product.objects.all()
    return render(request, 'products/news.html', {'products': products})
      

