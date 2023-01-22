import datetime
from django.db import models


class Card(models.Model):
    """Модель Бонусных карт (карт лояльности, кредитный карт и т.д.)"""

    STATUSES = (
        ('N', 'NOT_ACTIVATED'),
        ('A', 'ACTIVATED'),
        ('E', 'EXPIRED'),
    )

    series = models.CharField("Cерия", max_length=4)
    number = models.CharField("Номер", max_length=16, unique=True)

    issue_date = models.DateTimeField("Дата выпуска", auto_now_add=True)
    expiration_date = models.DateTimeField("Дата окончания действия")
    use_date = models.DateTimeField("Дата использования", null=True, blank=True)

    balance = models.FloatField("Баланс", default=0)

    status = models.CharField("Статус", choices=STATUSES, max_length=1, default='N')

    def __str__(self):
        return self.number


    @classmethod
    def card_generator(cls, count: int, last_number: str, expiration_date: datetime.datetime):
        """
            Генерирует count Card с series и expiration_date

            Args:
                count (int): кол-во создаваемых карт
                last_number (str): последняя карта с Card.series
                expiration_date (datetime.datetime): дата до которой действительна карта
            Returns
                created cards (list) список созданный карт

        """
        series = last_number[:4]
        int_last_number_without_series = int(last_number[4:])

        cards = [cls(
                    series=series,
                    number=series + str(int_last_number_without_series + i).rjust(12, '0'),
                    expiration_date=expiration_date,)
                 for i in range(1, count+1)]

        return cls.objects.bulk_create(cards)


    class Meta:
        verbose_name = 'Бонусная карта'
        verbose_name_plural = 'Бонусные карты'