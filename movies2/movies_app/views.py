from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.

def movies_list(request):
    # obtener todas las instancias del objeto en la base de datos
    allMovies = Movies.objects.all().order_by('id') 

    # validación de la búsqueda 
    movieName = request.GET.get('movie_name')
    if movieName != '' and movieName is not None:
        allMovies = allMovies.filter(name__icontains=movieName)
    # creación del Paginator
    paginator = Paginator(allMovies, 3)
    # obtener el numero de la pagina de la petición
    page = request.GET.get('page')
    # definir los items que van a ir en esta pagina
    items = paginator.get_page(page)
    return render(request, 'movies_list.html', {
        'movies': items,
    })