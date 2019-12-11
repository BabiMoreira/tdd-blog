from django.shortcuts import render
from .forms import PedidoForm


def home(request):
    return render(request, 'home.html')

def posts(request):
    return render(request, 'posts.html')

def cadastro(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        contexto = {
            'msg': 'Parabens, o seu pedido foi realizado com sucesso'
        }
        return render(request, 'cadastro.html', contexto)
    
    contexto = {
        'formulario': form
    }
    
    return render(request, 'cadastro.html', contexto)
    


