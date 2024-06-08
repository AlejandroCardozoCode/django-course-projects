from django.urls import path
from . import views

app_name = "food"
urlpatterns = [
    path("food/", views.IndexClassView.as_view(), name="index" ),
    path("<int:pk>/", views.DetailsClassView.as_view(), name="details" ),
    path("add/", views.CreateItemClassView.as_view(), name="create_item" ),
    path("update/<int:itemId>/", views.updateItem, name="update_item" ),
    path("delete/<int:itemId>/", views.deleteItem, name="delete_item" ),
]
