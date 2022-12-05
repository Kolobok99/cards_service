from django.db import models


class Card(models.Model):
    """Модель Бонусных карт (карт лояльности, кредитный карт и т.д.)"""

    STATUSES = (
        ('N', 'NOT_ACTIVATED'),
        ('A', 'ACTIVATED'),
        ('O', 'OVERDUE'),
    )

    series = models.CharField("Cерия", max_length=16)
    number = models.CharField("Номер", max_length=16)

    issue_date = models.DateTimeField("Дата выпуска")
    expiration_date = models.DateTimeField("Дата окончания действия")
    use_date = models.DateTimeField("Дата использования")

    balance = models.FloatField("Баланс")

    status = models.CharField("Статус", choices=STATUSES, max_length=1)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Бонусная карта'
        verbose_name_plural = 'Бонусные карты'