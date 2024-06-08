from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    allProducts = Product.objects.all()

    itemName = request.GET.get('item_name')

    # busqueda
    if itemName is not None and itemName != '':
        allProducts = allProducts.filter(name__icontains=itemName)

    
    # paginacion 
    paginator = Paginator(allProducts, 4)
    page = request.GET.get('page')

    items = paginator.get_page(page)
    context = {
        'products': items 
    }
    return render(request, 'shop/index.html', context)

def detail(request, id):
    product = Product.objects.get(id=id) 
    context = {
        'product': product 
    }

    return render(request=request, context=context, template_name='shop/detail.html')
