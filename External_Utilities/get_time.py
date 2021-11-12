import datetime as dt
from pytz import timezone


def now(config):
    time_zone = config['TIMEZONE']
    tz = timezone(time_zone)
    time_now = dt.datetime.now(tz)
    return time_now
