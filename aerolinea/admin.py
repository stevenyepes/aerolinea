from django.contrib import admin
from aerolinea.models import Cliente, Vuelo, Itinerario, Compania, Pasaje, Origen, Destino

class ClienteInline(admin.StackedInline):
	model = Cliente
		

class VueloInline(admin.StackedInline):
	model = Vuelo

class ItinerarioInline(admin.StackedInline):
	model = Itinerario


class CompaniaInline(admin.StackedInline):
	model = Compania

class PasajeInline(admin.StackedInline):
	model = Pasaje

class OrigenAdmin(admin.ModelAdmin):
	inlines = [ItinerarioInline]

class DestinoAdmin(admin.ModelAdmin):
	inlines = [ItinerarioInline]

admin.site.register(Cliente)
admin.site.register(Vuelo)
admin.site.register(Itinerario)
admin.site.register(Compania)
admin.site.register(Pasaje)
admin.site.register(Origen,OrigenAdmin)
admin.site.register(Destino,DestinoAdmin)


