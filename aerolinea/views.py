from django.shortcuts import render

from django.http import HttpResponse, Http404
from aerolinea.models import Cliente, Vuelo, Pasaje
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from aerolinea.form import ClienteForm, VueloForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone



def index(request):
	clientes = Cliente.objects.all()
	return render_to_response('aerolinea/index.html',{'clientes': clientes})

def vista_clientes(request):
	clientes = Cliente.objects.all()
	return render_to_response('aerolinea/vista_clientes.html',{'clientes':clientes})

def cliente_crear(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('vista_clientes')

	else:
			form = ClienteForm()
	return render_to_response('aerolinea/cliente_crear.html',{'form': form}, context_instance = RequestContext(request))

def vuelos(request):
	vuelos = Vuelo.objects.all()
	return render_to_response('aerolinea/vuelos.html',{'vuelos': vuelos})

def vuelo_crear(request):
	if request.method == 'POST':
		form = VueloForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('vuelos')
	else:
		form = VueloForm()
	return render_to_response('aerolinea/vuelo_crear.html',{'form': form}, context_instance = RequestContext(request))


def cliente_detalle(request,id_cliente):
	cliente = get_object_or_404(Cliente,pk=id_cliente)

	return render_to_response('aerolinea/cliente_detalle.html',{'cliente':cliente})

def cliente_editar(request,id_cliente):
	cliente = get_object_or_404(Cliente, pk=id_cliente)
	if request.method == 'POST':
		form = ClienteForm(request.POST, instance=cliente)
		if form.is_valid():
			form.save()
			return redirect('videojuegos')

	else:
		form = ClienteForm(instance=cliente)

	return render_to_response('aerolinea/cliente_editar.html',{'form': form}, context_instance = RequestContext(request))

def pasajes_cliente(request,id_cliente):
	pasajes = Pasaje.objects.filter(cliente= id_cliente)
	return render_to_response('aerolinea/pasajes_cliente.html',{'pasajes': pasajes})

def vuelo_detalle(request,id_vuelo):
	vuelo = get_object_or_404(Vuelo, pk=id_vuelo)
	return render_to_response('aerolinea/vuelo_detalle.html',{'vuelo': vuelo})

def pasajeros(request,id_vuelo):
	pasajes = Pasaje.objects.filter(vuelo = id_vuelo)
	return  render_to_response('aerolinea/pasajeros.html',{'pasajes': pasajes})
