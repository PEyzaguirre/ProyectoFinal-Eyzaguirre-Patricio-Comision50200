from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

 
urlpatterns = [
    
    #------------------------------- Rest ------------------------------------------------------

     #path('Flujos/', include('Flujos.urls')),
    path('', home, name = "home"),
    path('buscar', buscar, name = "buscar"),
    path('AboutMe', AboutMe, name='AboutMe'),
    
    #------------------------------- Locales ------------------------------------------------------

    path('Locales', ver_locales, name = "locales"),
    path('FormularioLocal', localForm, name = "FormularioLocal"),
    path('editarLocal/<id_local>/', updateLocal, name = "ActualizaLocal"),
    path('borrarLocal/<id_local>/', eliminaLocal, name = "BorraLocal"),


    #------------------------------- Productos ------------------------------------------------------

    path('Productos', ver_productos, name = "Productos"),
    path('FormularioProducto', productoForm, name = "FormularioProducto"),    
    path('buscarProd', buscarProd, name = "buscarProd"),
    path('editarProducto/<id_producto>/', updateProducto, name = "ActualizaProducto"),
    path('borrarProducto/<id_producto>/', deleteProducto, name="BorraProducto"),


    #------------------------------- Entregas ------------------------------------------------------

    path('Entregas', ver_entregas, name = "Entregas"),
    path('FormularioEntrega', entregaForm, name = "FormularioEntrega"),
    path('editarEntrega/<id_entrega>/', updateEntrega, name = "ActualizaEntrega"),
    path('borrarEntrega/<id_entrega>/', deleteEntrega, name="BorraEntrega"),
    path('buscar_despacho', buscarDespacho, name = "buscar_despacho"),

    #------------------------------- Repartidores ------------------------------------------------------

    path('Repartidores', ver_repartidores, name = "Repartidores"),
    path('FormularioRepartidor', repartidorForm, name = "FormularioRepartidor"),
    path('editarRepartidor/<id_repartidor>/', updateRepartidor, name = "ActualizaRepartidor"),
    path('borrarRepartidor/<id_repartidor>/', eliminaRepartidor, name = "BorraRepartidor"),


    #------------------------------- Login, Logout, Registro  ------------------------------------------------------

    path('login/', loguin_request, name = "login"),
    path('registro/', register, name = "registro"),
    path('logout/', LogoutView.as_view(template_name="Flujos/logout.html"), name="logout"),
    path('editar_perfil/', editarPerfil, name = "editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name = "agregar_avatar"),

]
