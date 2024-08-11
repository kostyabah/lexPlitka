from django.db import models
from django_jsonform.models.fields import JSONField
#https://rogulski.it/django-multiselect-choice-admin/
import datetime

class Articles(models.Model):
    image = models.ImageField('Загрузити фото', upload_to='uploads/product/')
    title = models.CharField('Назва', max_length=50, default='введите название')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Стаття')
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'

        
class Master(models.Model):
    name = models.CharField('Назва', max_length=100)
    
    image = models.ImageField('Загрузити фото', default='', upload_to='uploads/master/')
    phone =  models.CharField('Телефон', max_length=20, default='', blank=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    price = models.DecimalField('Ціна',default=0, decimal_places=2, max_digits=6)       
    description = models.CharField('Опис',max_length=250, default='', blank=True, null=True)
    
    LABELS_SCHEMA = {
        "type": "array",
        "items": {
            "type": "string",
            # "choices": ["blue", "red", "green"],
        },
    }

    addons_fields = JSONField(schema=LABELS_SCHEMA, null=True, blank=True)
    def __str__(self):
        return self.name


class Service(models.Model): 
    name = models.CharField('Послуга', max_length=50)
    image = models.ImageField('Загрузити фото', default='', upload_to='uploads/service/')
    phone =  models.CharField('Телефон', max_length=20, default='', blank=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    price = models.DecimalField('Ціна',default=0, decimal_places=2, max_digits=6)       
    description = models.CharField('Опис',max_length=250, default='', blank=True, null=True)
    
    LABELS_SCHEMA = {
        "type": "array",
        "items": {
            "type": "string",
            # "choices": ["blue", "red", "green"],
        },
    }

    addons_fields = JSONField(schema=LABELS_SCHEMA, null=True, blank=True)
    def __str__(self):
        return self.name
    

class SinkFromTile(models.Model): 
    name = models.CharField('Раковина з плитки', max_length=50)
    image = models.ImageField('Загрузити фото', default="", upload_to='uploads/sinkFromTile/')
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Категорія', max_length=50)
    image = models.ImageField('Загрузити фото', default='', upload_to='uploads/product/')
    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField('Назва', max_length=100)
    phone =  models.CharField('Телефон', max_length=20, default='', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    price = models.DecimalField('Ціна',default=0, decimal_places=2, max_digits=6)       
    description = models.CharField('Опис',max_length=250, default='', blank=True, null=True)
    image = models.ImageField('Загрузити фото', default='', upload_to='uploads/product/')
    date = models.DateField('Дата публікації',default=datetime.datetime.today)

    LABELS_SCHEMA = {
        "type": "array",
        "items": {
            "type": "string",
            # "choices": ["blue", "red", "green"],
        },
    }

    addons_fields = JSONField(schema=LABELS_SCHEMA, null=True, blank=True)
    def __str__(self):
        return self.name