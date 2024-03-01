from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms  import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    return render(request, "Flujos/home.html")


def AboutMe(request):
    return render(request, "Flujos/AboutMe.html")




#------------------------------- Locales ------------------------------------------------------

@login_required
def ver_locales(request):
    contexto = {'locales': Locales.objects.all()}
    return render(request, "Flujos/locales.html", contexto)


@login_required
def localForm(request):
    if request.method == "POST":
        miForm = LocalesForm(request.POST)
        if miForm.is_valid():
            local_nombre = miForm.cleaned_data.get("nombre")
            local_ubicacion = miForm.cleaned_data.get("ubicacion")
            newLocal = Locales(nombre=local_nombre,ubicacion=local_ubicacion)
            newLocal.save()
            return render(request, "Flujos/home.html") 
    else:
        miForm = LocalesForm()

    return render(request, "Flujos/localForm.html", {"form": miForm}) 


@login_required
def updateLocal(request, id_local):
    local = Locales.objects.get(id=id_local)
    if request.method == "POST":
        miForm = LocalesForm(request.POST)
        if miForm.is_valid():
            local.nombre = miForm.cleaned_data.get('nombre')
            local.ubicacion = miForm.cleaned_data.get('ubicacion')
            local.save()
            return redirect(reverse_lazy("locales"))   
    else:
            miForm = LocalesForm(initial={
                'nombre': local.nombre,
                'ubicacion': local.ubicacion,
            })

    return render(request, "Flujos/localForm.html", {'form': miForm})        


@login_required
def eliminaLocal(request, id_local):
    local = Locales.objects.get(id=id_local)
    local.delete()
    return redirect(reverse_lazy("locales"))


#------------------------------- Repartidor ------------------------------------------------------

@login_required
def ver_repartidores(request):
    contexto = {'repartidores': Repartidor.objects.all()}
    return render(request, "Flujos/repartidores.html", contexto)


@login_required
def repartidorForm(request):
    if request.method == "POST":
        miForm = RepartidorForm(request.POST)
        if miForm.is_valid():
            rep_nombre = miForm.cleaned_data.get("nombre")
            rep_rut = miForm.cleaned_data.get("rut")
            rep_direccion = miForm.cleaned_data.get("direccion")
            newRep = Repartidor(nombre=rep_nombre,rut=rep_rut, direccion = rep_direccion)
            newRep.save()
            return render(request, "Flujos/home.html") 
    else:
        miForm = RepartidorForm()
    
    return render(request, "Flujos/repartidorForm.html", {"form": miForm}) 


@login_required
def updateRepartidor(request, id_repartidor):
    reponedor = Repartidor.objects.get(id=id_repartidor)
    if request.method == "POST":
        miForm = RepartidorForm(request.POST)
        if miForm.is_valid():
            reponedor.nombre = miForm.cleaned_data.get('nombre')
            reponedor.rut = miForm.cleaned_data.get('rut')
            reponedor.direccion = miForm.cleaned_data.get('direccion')
            reponedor.save()
            return redirect(reverse_lazy("Repartidores"))   
    else:
            miForm = RepartidorForm(initial={
                'nombre': reponedor.nombre,
                'rut': reponedor.rut,
                'direccion': reponedor.direccion,
            })

    return render(request, "Flujos/repartidorForm.html", {'form': miForm})        


@login_required
def eliminaRepartidor(request, id_repartidor):
    reponedor = Repartidor.objects.get(id=id_repartidor)
    reponedor.delete()
    return redirect(reverse_lazy("Repartidores"))


#------------------------------- Productos ------------------------------------------------------

@login_required
def ver_productos(request):
    contexto = {'productos': Productos.objects.all()}
    return render(request, "Flujos/productos.html", contexto)


@login_required
def productoForm(request):
    if request.method == "POST":
        miForm = ProductosForm(request.POST)
        if miForm.is_valid():
            prod_nombre = miForm.cleaned_data.get("nombre")
            prod_umedida = miForm.cleaned_data.get("unidadMedida")
            prod_tipoprod = miForm.cleaned_data.get("tipoProducto")
            newProd = Productos(nombre=prod_nombre,unidadMedida=prod_umedida, tipoProducto = prod_tipoprod)
            newProd.save()
            return render(request, "Flujos/home.html") 
    else:
        miForm = ProductosForm()
    
    return render(request, "Flujos/productoForm.html", {"form": miForm}) 


@login_required
def buscar(request):
    return render(request, "Flujos/buscar.html")


@login_required
def buscarProd(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        prod = Productos.objects.filter(nombre__icontains=patron)
        contexto = {"productos": prod}
        return render(request, "Flujos/productos.html", contexto)
    return HttpResponse("No se ingresaron patrones de búsqueda")


@login_required
def updateProducto(request, id_producto):
    producto = Productos.objects.get(id=id_producto)
    if request.method == "POST":
        miForm = ProductosForm(request.POST)
        if miForm.is_valid():
            producto.nombre = miForm.cleaned_data.get('nombre')
            producto.unidadMedida = miForm.cleaned_data.get('unidadMedida')
            producto.tipoProducto = miForm.cleaned_data.get('tipoProducto')
            producto.save()
            return redirect(reverse_lazy("Productos"))   
    else:
            miForm = ProductosForm(initial={
                'nombre': producto.nombre,
                'unidadMedida': producto.unidadMedida,
                'tipoProducto': producto.tipoProducto,
            })

    return render(request, "Flujos/productoForm.html", {'form': miForm})        


@login_required
def deleteProducto(request, id_producto):
    producto = Productos.objects.get(id=id_producto)
    producto.delete()
    return redirect(reverse_lazy("Productos")) 


#------------------------------- Despachos ------------------------------------------------------

@login_required
def buscarDespacho(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        despacho = Entregas.objects.filter(producto__icontains=patron)
        contexto = {"entregas": despacho}
        return render(request, "Flujos/entregas.html", contexto)
    return HttpResponse("No se ingresaron patrones de búsqueda")


@login_required
def ver_entregas(request):
    contexto = {'entregas': Entregas.objects.all()}
    return render(request, "Flujos/entregas.html", contexto)


@login_required
def entregaForm(request):
    if request.method == "POST":
        miForm = EntregasForm(request.POST)
        if miForm.is_valid():
            entrega_fechaEntrega = miForm.cleaned_data.get("fechaEntrega")
            entrega_producto = miForm.cleaned_data.get("producto")
            entrega_cantidad = miForm.cleaned_data.get("cantidad")
            entrega_localDestino = miForm.cleaned_data.get("localDestino")
            entrega_reponedor = miForm.cleaned_data.get("reponedor")
            entrega_fechaVcto = miForm.cleaned_data.get("fechaVcto")            
            newEntrega = Entregas(fechaEntrega=entrega_fechaEntrega,producto=entrega_producto, cantidad = entrega_cantidad, localDestino=entrega_localDestino, reponedor=entrega_reponedor, fechaVcto=entrega_fechaVcto)
            newEntrega.save()
            return render(request, "Flujos/home.html") 
    else:
        miForm = EntregasForm()
    
    return render(request, "Flujos/entregaForm.html", {"form": miForm}) 


@login_required
def updateEntrega(request, id_entrega):
    entrega = Entregas.objects.get(id=id_entrega)
    if request.method == "POST":
        miForm = EntregasForm(request.POST)
        if miForm.is_valid():
            entrega.fechaEntrega = miForm.cleaned_data.get('fechaEntrega')
            entrega.producto = str(miForm.cleaned_data.get('producto'))
            entrega.cantidad = miForm.cleaned_data.get('cantidad')
            entrega.localDestino = str(miForm.cleaned_data.get('localDestino'))
            entrega.reponedor = str(miForm.cleaned_data.get('reponedor'))
            entrega.fechaVcto = miForm.cleaned_data.get('fechaVcto')
            entrega.save()
            return redirect(reverse_lazy("Entregas"))   
    else:
            miForm = EntregasForm(initial={
                'fechaEntrega': entrega.fechaEntrega,
                'producto': entrega.producto,
                'cantidad': entrega.cantidad,
                'localDestino': entrega.localDestino,
                'reponedor': entrega.reponedor,
                'fechaVcto': entrega.fechaVcto,
            })

    return render(request, "Flujos/entregaForm.html", {'form': miForm})        


@login_required
def deleteEntrega(request, id_entrega):
    entrega = Entregas.objects.get(id=id_entrega)
    entrega.delete()
    return redirect(reverse_lazy("Entregas")) 


#------------------------------- Login, Logout, Registro  ------------------------------------------------------

def loguin_request(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)

            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return redirect(reverse_lazy("home"))   
        else:
            return redirect(reverse_lazy("login"))   

    miForm = AuthenticationForm()
    
    return render(request, "Flujos/login.html", {"form": miForm}) 


def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            update_session_auth_hash(request, usuario)
            return redirect('home')
            # return redirect('/home')
            # return http.HttpResponseRedirect('')

    else:    
        miForm = RegistroForm()

    return render(request, "Flujos/registro.html ", {"form": miForm })  


@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "Flujos/home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "Flujos/editarPerfil.html", {"form": form }) 


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            # Borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            # ------
                    
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # URL de la imagen en request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "Flujos/home.html")

    else:    
        form = AvatarForm()

    return render(request, "Flujos/agregarAvatar.html", {"form": form })     