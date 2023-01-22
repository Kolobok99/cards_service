from rest_framework import serializers


class CardBalanceValidator:
    """
        Валидатор OrderSerializer

        Args:
            balance (Card.balance): баланс карты до покупки
            price (Product.price): цена товара
            count (int): кол-во покупаемых товаров

        Проверяет достаточно ли денег для покупки товара(ов)
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
