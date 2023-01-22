import datetime
import re

from django.core import validators
from rest_framework import serializers

from .models import Card
from apps.products.serializers import OrderSerializer


class CardSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Card"""

    orders = OrderSerializer(read_only=True, many=True)

    class Meta:
        model = Card
        fields = [
            'number',
            'issue_date',
            'expiration_date',
            'use_date',
            'balance',
            'status',
            'orders',
        ]


class CardGeneratorSerializer(serializers.Serializer):
    """
    Сериалайзер генерации Card
    """
    count = serializers.IntegerField(label='Кол-во карт')
    series = serializers.IntegerField(label='Серия',
                                      validators=[validators.MinValueValidator(1),
                                                  validators.MaxValueValidator(9999),
                                                  ]
                                      )
    expiration_date = serializers.CharField(label='Дата')

    def create(self, validated_data):
        return Card.card_generator(**validated_data)

    def validate(self, data: dict):
        series = str(data.pop('series'))

        data['expiration_date'] = datetime.datetime.today() + self.convert_date_string_to_timedelta(data['expiration_date'])
        data['last_number'] = getattr(Card.objects.filter(series=series)
                                                .order_by('number')
                                                .last(),
                                                'number', None) or series + '0000' * 3

        if int(data['last_number'][4:]) + data['count'] > 9999_9999_9999:
            raise serializers.ValidationError('count of cards out of series range!')
        return data

    @staticmethod
    def convert_date_string_to_timedelta(date_string):
        """
            Преобразует дату из date_string в timedelta(days)

            Args:
                date_string (str): дата в формате
                                   %Y год|года|лет %M месяц|месяца|месяцов %Y день|дня|дней
            Returns:
                timedetla(days)=преобразованная дата в кол-во дней

            Raise:
                ValidationError("Wrong date format")
        """

        regex = re.compile(
            r'((?P<years>\d+?) (год|года|лет){1}\s?)?((?P<months>\d+?) (месяц|месяца|месяцов){1} ?)?((?P<days>\d+?) (день|дня|дней){1})?')
        parts = regex.match(date_string).groupdict(default=0)
        days = int(parts.get('days')) + int(parts.get('months')) * 30 + int(parts.get('years')) * 365

        if days:
            return datetime.timedelta(days=days)
        raise serializers.ValidationError("Wrong date format")

