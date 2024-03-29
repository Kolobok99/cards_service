from django.db import models

from apps.cards.models import Card


class Product(models.Model):
    """
    Вспомогательная модель Продуктов,
    служащая для реализации логики покупок
    """

    name = models.CharField("Наименование", max_length=16, unique=True)
    price = models.FloatField("Цена")

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    """Модель заказа продукта"""

    product = models.ForeignKey("Product", on_delete=models.PROTECT, related_name='orders')
    count = models.PositiveIntegerField("Кол-во", default=1)
    date = models.DateTimeField("Дата заказа:", auto_now_add=True)

    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"{self.product} {self.card}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'