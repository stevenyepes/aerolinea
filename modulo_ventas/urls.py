from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'modulo_ventas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   	url(r'^admin/', include(admin.site.urls)),
    url(r'^aerolinea/$','aerolinea.views.index',name='aerolinea'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^aerolinea/vista_clientes/$','aerolinea.views.vista_clientes',name='vista_clientes'),
    url(r'^aerolinea/registrar/cliente/$','aerolinea.views.cliente_crear',name='cliente_crear'),
    url(r'^aerolinea/registrar/vuelo/$','aerolinea.views.vuelo_crear',name='vuelo_crear'),
    url(r'^aerolinea/vuelos/$','aerolinea.views.vuelos',name='vuelos'),
    url(r'^aerolinea/(?P<id_cliente>\d+)/$','aerolinea.views.cliente_detalle',name='cliente_detalle'),
    url(r'^aerolinea/editar/(?P<id_cliente>\d+)/$','aerolinea.views.cliente_editar',name='cliente_editar'),
    url(r'^aerolinea/cliente/pasajes/(?P<id_cliente>\d+)/$','aerolinea.views.pasajes_cliente',name='pasajes_cliente'),
    url(r'^aerolinea/vuelos/(?P<id_vuelo>\d+)/$','aerolinea.views.vuelo_detalle',name='vuelo_detalle'),
    url(r'^aerolinea/vuelos/pasajeros/(?P<id_vuelo>\d+)/$','aerolinea.views.pasajeros',name='pasajeros'),
)
