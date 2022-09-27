from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('home')

