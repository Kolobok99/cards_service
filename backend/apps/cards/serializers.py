from rest_framework import serializers

from .models import Card
from apps.products.models import Order
from apps.products.serializers import OrderSerializer


class CardSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Card"""

    orders = OrderSerializer(read_only=True, many=True)

    class Meta:
        model = Card
        fields = [
            'id',
            'number',
            'issue_date',
            'expiration_date',
            'use_date',
            'balance',
            'status',
            'orders',
        ]