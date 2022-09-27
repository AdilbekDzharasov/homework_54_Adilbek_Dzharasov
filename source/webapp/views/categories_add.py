from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Category


def category_add_view(request):
    if request.method == "GET":
        return render(request, "add_category.html")
    category_data = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
    }
    category = Category.objects.create(**category_data)
    return redirect('home')

