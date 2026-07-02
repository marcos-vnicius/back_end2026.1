from django.contrib import admin
from .models import Usuario, Livro, Emprestimo, Conta

admin.site.register(Usuario)
admin.site.register(Livro)
admin.site.register(Emprestimo)
admin.site.register(Conta)
