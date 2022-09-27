from django.contrib import admin

from webapp.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'categories', 'price']
    list_filter = ['id', 'name', 'description', 'categories', 'price', 'created_at']
    search_fields = ['id', 'name']
    fields = ['id', 'name', 'description', 'categories', 'price', 'created_at']
    readonly_fields = ['id']


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['id', 'name', 'description']
    search_fields = ['id', 'name']
    fields = ['id', 'name', 'description']
    readonly_fields = ['id']


admin.site.register(Category, CategoryAdmin)

