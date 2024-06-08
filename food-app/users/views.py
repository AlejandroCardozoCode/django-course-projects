from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import RegisterFrom

# Create your views here.

def register(request):
    # si la petición es post entonces crear el usuario
    if request.method == "POST":
        # cargar el formulario personalizado
        form = RegisterFrom(request.POST)
        # verificar que el formulario es valido
        if form.is_valid():
            # guardar el usuario en la base de datos
            form.save()
            # redirigir a la pagina de inicio
            return redirect("login")

    else:
        # en caso de que la petición sea un GET entonces renderizar la pantalla del formulario
        form = RegisterFrom()

    return render(request, "users/register.html",
        { 
            "form": form
        })

@login_required
def profilePage(request):
    return render(request,"users/profile.html" )