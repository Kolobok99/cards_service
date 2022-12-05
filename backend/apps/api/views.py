from rest_framework import viewsets

from apps.cards.models import Card
from apps.cards.serializers import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    """ViewSet модели Card"""

    queryset = Card.objects.all()
    serializer_class = CardSerializer
