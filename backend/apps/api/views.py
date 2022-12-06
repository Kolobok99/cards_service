from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


from apps.cards.models import Card
from apps.cards.serializers import CardSerializer
from services.filtration import CardFilter
from services.services import card_generator, convert_date_string_to_timedelta


class CardListAndDestroyAPIView(ListAPIView, CreateAPIView, DestroyAPIView):
    """ListAPIView,DestroyAPIView модели Card"""

    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_field = 'number'
    filterset_class = CardFilter


class CardGenerator(APIView):
    """Контроллер генерации карт"""

    def post(self, request, *args, **kwargs):
        count: str = request.data.get('count')
        series: str = request.data.get('series')
        expiration_date: str = request.data.get('expiration_date')

        if (count and series and expiration_date) \
                and (count.isdigit() and series.isdigit()) \
                and convert_date_string_to_timedelta(expiration_date):
            message = card_generator(int(count), series, convert_date_string_to_timedelta(expiration_date))
            return Response(message)
        else:
            return Response({'message': "Bad Request"}, 400)


class CardActivateOrDeactivate(RetrieveAPIView):
    """Контроллер Активации/Деактивации карты"""

    queryset = Card.objects.all()
    lookup_field = 'number'
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):

        card = self.get_object()
        if card.status == 'N':
            card.status = 'A'
            card.save()
            return Response({'message': f'Card ({card.number}) activated!'}, 200)
        elif card.status == 'A':
            card.status = 'N'
            card.save()
            return Response({'message': f'Card ({card.number}) DEactivated!'}, 200)
        else:
            return Response({'message': f'Card ({card.number} is expired!)'}, 400)