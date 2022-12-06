from django.db import models

# Create your models here.

class Product(models.Model):
    """
    Вспомогательная модель Продуктов,
    служащая для реализации логики покупок модели card.Card
    """

    name = models.CharField("Наименование", max_length=16, unique=True)
    price = models.FloatField("Цена")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    """Модель заказа продукта"""

    product = models.ForeignKey("Product", on_delete=models.PROTECT, related_name='orders')
    count = models.PositiveIntegerField("Кол-во", default=1)
    date = models.DateTimeField("Дата заказа:", auto_now_add=True)

    card = models.ForeignKey("Card", on_delete=models.CASCADE, related_name='orders')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'