from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'nome',
            'email',
            'cartao',
            'pagamento',
        ]

# criamos esse arquivo forms para utilizarmos o formulario
# do proprio django.