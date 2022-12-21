from django.contrib import admin

from primeira_app.models import Autor, Livro, Categoria, Endereco, Cliente


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    ...


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    pass


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    pass

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass
