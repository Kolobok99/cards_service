import datetime

from rest_framework import serializers

from .models import Order, Product
from .validators import CardBalanceValidator


class ProductSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Product"""

    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Order"""

    def create(self, validated_data):
        """Изменяет card.balance и card.use_date перед созданием заказа"""

        card = validated_data.get('card')
        count = validated_data.get('count')
        product = validated_data.get('product')

        card.balance = card.balance - count*product.price
        card.use_date = datetime.datetime.today()
        card.save()

        return super().create(validated_data)

    class Meta:
        model = Order
        fields = "__all__"
        validators = [CardBalanceValidator]