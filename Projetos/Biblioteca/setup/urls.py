"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from biblioteca.views import index, cadastro_usuario, conta, emprestimos, listar_livros, listar_usuarios, cad_livros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="inicio"),
    path('cadastrar/', cadastro_usuario, name="cadastro"),
    path('emprestimos/', emprestimos, name='listar_emprestimos'),
    path('cadastrar_livros/', cad_livros, name='cadastrar_livros'),
    path('lista_livros/', listar_livros, name='listar_livros'),
    path('lista_usuarios/', listar_usuarios, name='listar_usuarios'),
    path('conta/<int:conta_id>/', conta, name='conta')
]
