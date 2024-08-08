from django.contrib import admin
from .models import Category, Product, Service, Master, SinkFromTile


#admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(SinkFromTile)
admin.site.register(Master)