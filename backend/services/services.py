import datetime
import re
from datetime import timedelta

from apps.cards.models import Card


def card_generator(count, series, expiration_date_delta):

    expiration_date = datetime.datetime.today() + expiration_date_delta

    last_card = Card.objects.filter(series=series).order_by('number').last()

    if not last_card:
        last_card = Card.objects.create(
            series=series,
            number=series + '0000'*3,
            expiration_date=expiration_date,

        )
        count -= 1
    last_number = last_card.number
    int_last_number = int(last_number)
    if int(str(last_number)[5:]) + count + 1 > 999999999999:
        return ({'message': 'Card count out of series range!'},400)

    for i in range(1, count+1):
        Card.objects.create(
            series=series,
            number=series + (int_last_number[5:] + i),
            expiration_date=expiration_date,
        )
    return ({"message": 'Card successfully generated!'},200)


def convert_date_string_to_timedelta(date_string):
    """Преобразует дату из строки в timedelta"""

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
