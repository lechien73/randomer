from random import randrange
from datetime import timedelta, datetime

def random_date(end):
    """
    Return a random date string between two datetime 
    objects.
    """
    start = datetime.strptime("1989-03-17", "%Y-%m-%d")
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    rand_date = start + timedelta(seconds=random_second)
    return rand_date.strftime("%Y-%m-%d")
