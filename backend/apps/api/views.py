from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.cards.models import Card
from apps.cards.serializers import CardSerializer, CardGeneratorSerializer

from apps.products.models import Order, Product
from apps.products.serializers import OrderSerializer, ProductSerializer

from services.filtration import CardFilter


class CardAPIViewSet(ModelViewSet):
    """APIViewSet модели Card """
    queryset = Card.objects.all().prefetch_related('orders')
    serializer_class = CardSerializer
    lookup_field = 'number'
    filterset_class = CardFilter

    @action(detail=False, methods=['post'])
    def generation(self, request, pk=None):
        """
            Генерирует набор карт
            Args:
                series (int): серия
                count (int): кол-во создаваемых карт
                expiration_date (str): дата в формате
                                       %Y год|года|лет %M месяц|месяца|месяцов %Y день|дня|дней
        """
        serializer = CardGeneratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Cards successfully created!", 201)
        else:
            return Response(serializer.errors, 400)

    @action(detail=True, methods=['get'])
    def activate(self, request, number=None):
        """
        Активация/Деактивация карт
        """
        card = self.get_object()
        if card.status == 'N':
            card.status = 'A'
            card.save()
            return Response({'message': f'Card ({card.number}) activated!'}, 200)
        elif card.status == 'A':
            card.status = 'N'
            card.save()
            return Response({'message': f'Card ({card.number}) deactivated!'}, 200)
        else:
            return Response({'message': f'Card ({card.number} is expired!)'}, 400)


class ProductAPIViewSet(ModelViewSet):
    """APIViewSet модели Product"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderAPIViewSet(ModelViewSet):
    """APIViewSet модели Order с запрещенным изменением записи"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['head', 'options', 'get', 'post', 'delete']