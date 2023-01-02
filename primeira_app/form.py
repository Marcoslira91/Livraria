from django.forms import ModelForm
from .models import Livro, Carrinho

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ["titulo", "autor", "descricao", "valor", "categoria", "genero", "isbn"]


class CarrinhoForm(ModelForm):
    class Meta:
        model = Carrinho
        fields = ['produto', 'quantidade']
