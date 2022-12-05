from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Card"""

    class Meta:
        model = Card
        fields = "__all__"