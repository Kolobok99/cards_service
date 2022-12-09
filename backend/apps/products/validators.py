from rest_framework import serializers


class CardBalanceValidator:
    """
        Валидатор OrderSerializer

        Args:
            time_interval_start (Mailing.time_interval_start): начала временного интервала
            time_interval_end (Mailing.time_interval_end): конец временного интервала

        Если переданы оба значения, проверяет, что конец не превышает начала интервала
    """

    requires_context = True

    def __init__(self, data, serializer):
        self.__call__(data, serializer)

    def __call__(self, data, serializer):
        errors = {}

        card = data.get('card')
        product = data.get('product')
        count = data.get('count')

        if card.balance < product.price * count:
            errors['balance_error'] = 'Ошибка: Не достаточно баланса для оплаты заказа'

        if errors:
            raise serializers.ValidationError(errors)
