from django.shortcuts import render,redirect
from .models import Afiliado, Practica , Pedido
from .forms import AfiliadoForm, PracticaForm, PedidoForm, AfiliadoSearchForm
from django.db.models import Count





def index(request):
    return render(request,'autorizaciones/index.html')

def afiliado_list(request):
    query = Afiliado.objects.all()
    context = {"object_list": query}
    return render(request, "autorizaciones/afiliado_list.html", context)

def pedido_list(request):
    pedidos = Pedido.objects.all()

    pedidos_pendientes = pedidos.filter(estado='pendiente')
    pedidos_aprobados = pedidos.filter(estado='aprobada')
    pedidos_rechazados = pedidos.filter(estado='rechazada')

    pedidos_por_estado = pedidos.values('estado').annotate(total=Count('id'))

    context = {
        'pedidos': pedidos,
        'pedidos_pendientes': pedidos_pendientes,
        'pedidos_aprobados': pedidos_aprobados,
        'pedidos_rechazados': pedidos_rechazados,
        'pedidos_por_estado': pedidos_por_estado,
    }
    return render(request, "autorizaciones/pedido_list.html", context)

def practica_list(request):
    query = Practica.objects.all()
    context = {"object_list": query}
    return render(request, "autorizaciones/practica_list.html", context)
    





def afiliado_create(request):
    if request.method =="GET":
        form = AfiliadoForm()
    if request.method == "POST":
        form = AfiliadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("afiliado_list")
    return render(request, "autorizaciones/afiliado_create.html",{"form":form} )

def pedido_create(request):
    if request.method =="GET":
        form = PedidoForm()
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pedido_list")
    return render(request, "autorizaciones/pedido_create.html", {"form": form})


def practica_create(request):
    if request.method =="GET":
        form = PracticaForm()
    if request.method == "POST":
        form = PracticaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("practica_list")
    return render(request, "autorizaciones/practica_create.html", {"form": form})



def buscar_afiliado(request):
    form = AfiliadoSearchForm(request.GET or None)
    resultados = None

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        apellido = form.cleaned_data.get('apellido')
        email = form.cleaned_data.get('email')
        dni = form.cleaned_data.get('dni')

        afiliados = Afiliado.objects.all()

        if nombre:
            afiliados = afiliados.filter(nombre__icontains=nombre)
        if apellido:
            afiliados = afiliados.filter(apellido__icontains=apellido)
        if email:
            afiliados = afiliados.filter(email__icontains=email)
        if dni:
            afiliados = afiliados.filter(dni__icontains=dni)

        resultados = Pedido.objects.filter(afiliado__in=afiliados).select_related('practica')

    return render(request, 'autorizaciones/buscar_afiliado.html', {'form': form, 'resultados': resultados})