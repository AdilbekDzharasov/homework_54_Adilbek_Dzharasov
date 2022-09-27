from django.urls import path

from webapp.views.base import products_view
from webapp.views.products_add import product_add_view
from webapp.views.products_add import product_view
from webapp.views.categories_add import category_add_view

urlpatterns = [
    path('', products_view, name='home'),
    path('products/add/', product_add_view, name='products_add'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('categories/add/', category_add_view, name='categories_add'),
]

