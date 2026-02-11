from django.db import models
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime 

class Contact(models.Model):
    name=models.CharField("Ім'я", max_length = 200)
    email=models.EmailField('Пошта')
    phone = models.CharField('Телефон', max_length=13)
    subject=models.TextField('Тема запиту')
    date=models.DateTimeField('День та час коли  зателефонувати')
    

    def __str__(self):
        return self.name



    # name = models.CharField('Введіть ваше імя (обовязково)', max_length=50)
    # email = models.EmailField('Введіть ваш e-mail (необовязково)')
    # phone = models.CharField('Введіть ваш телефон (обовязково)', max_length=13)
    # subject = models.TextField('Введіть ваше повідомлення (необовязково)')
    # date = models.DateTimeField()
    # def __str__(self):
    #     return self.name