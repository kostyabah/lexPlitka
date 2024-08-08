
from django.urls import path,include
from  . import views

urlpatterns = [

    #path('', views.contacts,name='button'),
    path('order_form', views.order_form,name='order_form')
]

# path('admin/', admin.site.urls),
    # path('', include('button.urls')),


