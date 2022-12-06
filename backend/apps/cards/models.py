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

    class Meta:
        verbose_name = 'Бонусная карта'
        verbose_name_plural = 'Бонусные карты'