from django.urls import path, include
from . import views
from main import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.index, name='home'),
   path('gallery/',views.imagedisplay, name='gallery'),
   path('services/', views.services, name='services'),
   path('masters/', views.masters, name='masters'),
   path('products/', views.products, name='products'),
   #path('gallery/', views.gallery, name='gallery'),
   path('about/', views.about, name='about'),
   path('contacts/', views.contacts, name='contacts'),
   path('contacts', include('button.urls')),
   path('news', include('news.urls')),
 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
