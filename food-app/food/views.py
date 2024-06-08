from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template import loader
from food.forms import ItemForm
from food.models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# # Create your views here.
# def index(request):
#     itemLIst = Item.objects.all()
#     context = {
#         "items": itemLIst,
#     }
#     return render(request=request, template_name="food/productsList.html", context=context)

# class base view
class IndexClassView(ListView):
    model = Item;
    template_name = "food/productsList.html"
    context_object_name = "items"

# def itemDetails(request, itemId):
#     item = Item.objects.get(id=itemId)
#     context = {
#         "item": item,
#     }
#     return render(request=request, template_name="food/details.html", context=context)

class DetailsClassView(DetailView):
    model = Item
    template_name = "food/details.html"
    context_object_name = "item"

# def createItem(request):
#     form = ItemForm(request.POST or None)

#     if form.is_valid():
#         form.save()

#         return redirect("food:index")
#     return render(request, "food/create-item-form.html", 
#         {
#         "form": form
#         })

class CreateItemClassView(CreateView):
    model = Item
    fields = ["name", "description", "price", "image"]
    template_name = "food/create-item-form.html"

    def formValid(self, form):
        form.instance.user = self.request.user
        return super().formValid(form)

def updateItem(request, itemId):
    item = Item.objects.get(id=itemId)

    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request, "food/create-item-form.html", 
        {
        "form": form,
        "item": item
        })

def deleteItem(request, itemId):
    item = Item.objects.get(id=itemId)

    if request.method == "POST":
        item.delete()
        return redirect("food:index")

    return render(request, "food/details.html", 
        {
            "item": item,
        })
