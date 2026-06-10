from django.contrib import admin

# Register your models here.

from .models import Cliente

#Registrar nosso modelo no ambiente admin do Django
admin.site.register(Cliente)