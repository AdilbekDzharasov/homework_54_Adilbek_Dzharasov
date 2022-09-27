from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product, Category


def get_category(request):
    categories = Category.objects.filter(name=f"{request.POST.get('categories')}")
    for category in categories:
        return Category.objects.get(pk=category.id)


def get_category_name():
    category = Category.objects.values('name')
    return category


def product_add_view(request):
    if request.method == "GET":
        category = get_category_name()
        return render(request, "add_product.html", context={'category': category})
    product_data = {
        'name': request.POST.get('name'),
        'price': request.POST.get('price'),
        'image': request.POST.get('image'),
        'categories': get_category(request),
        'description': request.POST.get('description'),
    }
    product = Product.objects.create(**product_data)
    return redirect('product_detail', pk=product.pk)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})

