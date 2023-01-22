import datetime

from django.db.transaction import atomic
from rest_framework import serializers

from .models import Order, Product
from .validators import CardBalanceValidator
from apps.cards.models import Card


class ProductSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Product"""

    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Order"""

    @atomic
    def create(self, validated_data):
        """Изменяет card.balance и card.use_date перед созданием заказа"""

        card = Card.objects.get(number=validated_data.get('card').number)
        product = Product.objects.get(name=validated_data.get('product').name)

        card.balance = card.balance - validated_data.get('count')*product.price
        card.use_date = datetime.datetime.today()
        card.save()

        return super().create(validated_data)

    class Meta:
        model = Order
        fields = ('product', 'count', 'date','card')
        validators = [CardBalanceValidator]