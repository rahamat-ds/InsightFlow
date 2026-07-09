from datetime import datetime, timedelta
import random

ORDER_START_DATE = datetime(2024, 1, 1)
ORDER_END_DATE = datetime(2025, 12, 31)


def random_order_date():

    delta = ORDER_END_DATE - ORDER_START_DATE

    return ORDER_START_DATE + timedelta(
        days=random.randint(0, delta.days)
    )