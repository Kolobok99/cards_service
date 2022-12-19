import datetime
import re
from datetime import timedelta

from apps.cards.models import Card


def card_generator(count, series, expiration_date_delta):
    """
        Генерирует count Card с series и expiration_date

        Args:
            count (int): кол-во создаваемых карт
            series (str): Card.series = series
            expiration_date_delta (timedelta): срок действия карты в timedelta
        Returns
            Success (200) - карты успешно созданы
            Bad request(400)
                            - Card count out of series range!

    """

    expiration_date = datetime.datetime.today() + expiration_date_delta

    # Получаем последнюю карту с series, иначе создаем первую
    last_card = Card.objects.filter(series=series).order_by('number').last()

    if not last_card:
        last_card = Card.objects.create(
            series=series,
            number=series + '0000'*3,
            expiration_date=expiration_date,

        )
        count -= 1

    int_last_number_without_series = int(last_card.number[5:])

    # проверяем возможность создания count карт
    if int_last_number_without_series + count > 999999999999:
        return ({'message': 'Card count out of series range!'},400)

    # генерируем карты
    for i in range(1, count+1):
        Card.objects.create(
            series=series,
            number=series + str(int_last_number_without_series + i),
            expiration_date=expiration_date,
        )
    return ({"message": 'Card successfully generated!'},200)


def convert_date_string_to_timedelta(date_string):
    """
        Преобразует дату из date_string в timedelta(days)

        Args:
            date_string (str): дата в формате
                               %Y год|года|лет %M месяц|месяца|месяцов %Y день|дня|дней
        Returns
            timedetla(days) - days=преобразованная дата в кол-во дней
            False - дата переданна в неверном формате

    """

    regex = re.compile(
        r'((?P<years>\d+?) (год|года|лет){1}\s?)?((?P<months>\d+?) (месяц|месяца|месяцов){1} ?)?((?P<days>\d+?) (день|дня|дней){1})?')
    parts = regex.match(date_string)
    parts = parts.groupdict()
    if not(parts.get('years') or parts.get('months') or parts.get('days')):
        return False

    days = 0
    for name, param in parts.items():
        if param:
            if name == 'year':
                days += int(param)*365
            elif name == 'months':
                days += int(param) * 30
            else:
                days += int(param)
    return timedelta(days=days)
