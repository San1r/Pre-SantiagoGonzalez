from django import forms
from .models import Afiliado, Practica, Pedido


class AfiliadoForm(forms.ModelForm):
    class Meta:
        model = Afiliado
        fields = "__all__"
    

class PracticaForm(forms.ModelForm):
    class Meta:
        model = Practica
        fields = "__all__"
    

    
class PedidoForm(forms.ModelForm):
     class Meta:
        model = Pedido
        fields = "__all__"



class AfiliadoSearchForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)
    apellido = forms.CharField(max_length=50, required=False)
    email = forms.CharField(max_length=100, required=False)
    dni = forms.CharField(max_length=8, required=False)