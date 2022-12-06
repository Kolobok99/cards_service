from datetime import datetime

from apps.cards.models import Card
from conf.celery import app


@app.task
def task_check_expiration_date() -> None:
    """TASK: изменяет статус card на EXPRESION у которых expiration_date > today """

    today = datetime.today()
    cards = Card.objects.filter(expiration_date__gt=today)
    cards.update(status='E')
