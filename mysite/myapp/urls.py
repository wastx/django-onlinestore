from django.urls import path
from myapp.views import add_item, update_item, delete_item, ProductListView, ProductDetailView, ProductDeleteView


app_name = "myapp"

urlpatterns = [

    path('', ProductListView.as_view(), name='index'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),

    path("additem/", add_item, name="add_item"),
    path("updateitem/<int:id>/", update_item, name="update_item"),
    path("deleteitem/<int:pk>/", ProductDeleteView.as_view(), name="delete_item"),

]
