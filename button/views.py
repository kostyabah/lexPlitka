from django.shortcuts import render, redirect
from .models import Contact
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages


def contacts(request):
    
    return render(request, 'contacts.html')



def order_form(request):
    if request.method == "POST":
        contact = Contact()
        fname = request.POST.get('name')
        # femail = request.POST.get('email')
        fphone = request.POST.get('phone')
        fsubject = request.POST.get('subject')
        fdate = request.POST.get('date')
        query=Contact(name=fname,phone=fphone,subject=fsubject,date = fdate)
        query.save()
        # contact.name = fname
        # contact.email = femail
        # contact.phone = fphone
        # contact.subject = fsubject
        # contact.date = fdate
        # contact.save()
        messages.info(request, "Повідомлення було надіслано")
        
        # return HttpResponse("<h2>Повідомлення було надіслано</h>")

       

    return render(request, 'button/order_form.html')



# def order_form(request):
#     error = ''

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("<h2>Повідомлення було доставлено</h2>")

#         else:
#             return HttpResponse("<h2>Неправильно введені дані</h2>")   

#     form = ContactForm()

#     data = {
#         'form': form,
#         'error': error
#     }

#     return render(request, 'button/order_form.html', data)




