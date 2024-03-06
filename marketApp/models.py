from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='category/', **NULLABLE, verbose_name='Фото')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=50, **NULLABLE, verbose_name='Наименование')
    photo = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Фото')
    descriptions = models.TextField(**NULLABLE, verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.CharField(max_length=30, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='в наличии')
    country = models.CharField(max_length=100, **NULLABLE, verbose_name='Страна')

    def __str__(self):
        return f'{self.name, self.category, self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
