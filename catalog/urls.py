from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, ContactsCreateView, ProductsListView, Category_ProductsListView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('category_product/<int:id>/', Category_ProductsListView.as_view(), name='category_product'),
    path('', home, name='home'),
]