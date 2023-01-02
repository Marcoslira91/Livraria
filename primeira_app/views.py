from django.shortcuts import render, redirect
from datetime import datetime
from .models import Livro, Carrinho, Shop, Cliente
from .form import LivroForm, CarrinhoForm

def home(request):
    dados = {"agora": datetime.now()}
    return render(request, "primeira_app/home.html", dados)


def listagem(request):
    dados = {"livros": Livro.objects.all()}
    return render(request, "primeira_app/listagem.html", dados)


def criar(request):
    dados = {}
    form = LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagem")

    dados["form"] = form
    return render(request, "primeira_app/form.html", dados)


def update(request, pk):
    dados = {}
    livro = Livro.objects.get(pk=pk)
    form = LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect("url_listagem")

    dados["form"] = form
    dados["livro"] = livro
    return render(request, "primeira_app/form.html", dados)


def delete(request, pk):
    livro = Livro.objects.get(pk=pk)
    livro.delete()
    return redirect("url_listagem")


def shopping_items_add(request):
    cliente = Cliente.objects.get(email=request.user.email)
    dados = {}
    form = CarrinhoForm(request.POST or None)

    if form.is_valid():
        form.instance.shop = Shop.objects.create(nome_cliente = cliente)
        form.save()

    dados["form"] = form
    
    return render(request, "primeira_app/carrinho_form.html", dados)

# def shopping_items_add(request):
#     request = request.POST
#     cliente = request.get("Cliente")
#     produtos = request.get("Produtos")

#     shop = Shop.objects.create(cliente=cliente)

#     for produtos in produtos:
#         product_obj = Product.objects.get(pk=product['pk'])
#         quantidade = product_obj['quantidade']
#         preco = product_obj['preco']

#         Cart.objects.create(
#             shop=shop,
#             product=product_obj,
#             quantity=quantidade,
#             price=preco
#         )
#     response = {'data': shop.pk}
#     return JsonResponse(response)


def cart_items(request, pk):
    template_name = 'cart_items.html'
    carts = Cart.objects.filter(shop=pk)

    qs = carts.values_list('price', 'quantity') or 0
    total = sum(map(lambda q: q[0] * q[1], qs))

    context = {'object_list': carts, 'total': total}
    return render(request, template_name, context)