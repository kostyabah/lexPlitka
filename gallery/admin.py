from django.contrib import admin
from .models import imggal

class resultsdisplayAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# Register your models here.
admin.site.register(imggal, resultsdisplayAdmin)