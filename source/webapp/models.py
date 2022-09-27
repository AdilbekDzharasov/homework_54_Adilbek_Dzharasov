from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    categories = models.ForeignKey(
        verbose_name='Категория',
        to = 'webapp.Category',
        null=False,
        blank=False,
        related_name='categories',
        on_delete=models.RESTRICT,
        default=None
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Стоимость')
    image = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f"{self.name} - {self.categories}"


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f"{self.name} - {self.description}"

