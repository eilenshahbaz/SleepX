""" Calculate what time to wake up and go to sleep """


def wake_up_time(hour, mins, cycles=6):
    """
    Given HOUR, MIN, and CYCLES, calculates wake time to
    wake up from this HOUR, MIN if asleep for that number of
    CYCLES. In military time.

    >>> wake_up_time(24, 0, 1)
    (1, 30)
    >>> wake_up_time(24, 0, 2)
    (3, 0)
    >>> wake_up_time(23, 30, 5)
    (7, 0)
    >>> wake_up_time(1, 10, 2)
    (4, 10)
    >>> wake_up_time(13, 10, 4)
    (19, 10)

    :param hour: int [1, 24]
    :param min: int [0, 60]
    :param cycles: the number of 90 minute cycles
    :return: int tuple (hour, minute) of wake up time
    """
    assert 1 <= hour <= 24
    assert 0 <= mins <= 60
    cycl_hrs = (cycles * 90) // 60
    cycl_mins = (cycles * 90) % 60
    hour += cycl_hrs
    mins += cycl_mins

    add_hrs, mins = mins_to_hour(mins)
    hour += add_hrs

    return adjust_military(hour, mins)


def adjust_military(hrs, mins):
    """
    Takes HRS, MINS and adjusts them to
    24 hour military time.

    >>> adjust_military(27, 45)
    (3, 45)
    >>> adjust_military(14, 50)
    (14, 50)

    :param hrs: int
    :param mins: int
    :return: int tuple (HOURS, MINS)
    """
    assert mins <= 60
    hrs = hrs % 24
    if hrs == 0:
        hrs = 24
    return hrs, mins


def mins_to_hour(minutes):
    """
    Takes MINUTES and any excess minutes over 60
    are turned into an hour. Returns (hour, mins).

    >>> mins_to_hour(90)
    (1, 30)
    >>> mins_to_hour(61)
    (1, 1)
    >>> mins_to_hour(45)
    (0, 45)

    :param minutes: int
    :return: int tuple of (hour, mins)
    """
    hrs = 0
    while minutes >= 60:
        hrs += 1
        minutes -= 60
    return hrs, minutes


def when_to_sleep(hour, mins, cycles=6):
    """
    Takes the desired time HOUR, MINS the user would
    like to wake up at and returns the tuple of
    (hour, mins) the user should go to sleep at.

    >>> when_to_sleep(1, 30, 1)
    (24, 0)
    >>> when_to_sleep(8, 0, 6)
    (23, 0)
    >>> when_to_sleep(4, 10, 2)
    (1, 10)

    :param hour: int -- desired time to wake up
    :param mins: int -- desired minute to wake up
    :param cycles: int -- number of desired cycles
    :return: int tuple (hour, mins) user should sleep
    """
    assert 1 <= hour <= 24
    assert 0 <= mins <= 60
    cycl_hrs = (cycles * 90) // 60
    cycl_mins = (cycles * 90) % 60

    hour -= cycl_hrs
    mins -= cycl_mins

    add_hrs, mins = mins_to_hour(mins)
    hour += add_hrs

    return adjust_military(hour, mins)