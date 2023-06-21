import time
from datetime import datetime

from dateutil import parser


def datetime_to_timestamp(datetime_str):
    date_object = parser.isoparse(str(datetime_str))
    timestamp = int(datetime.timestamp(date_object))
    return timestamp


def get_utc_datetime():
    return datetime.utcnow()


def get_custom_datetime():
    return datetime.utcnow()


def get_datetime():
    return datetime.now()


def timestamp_to_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp).isoformat()


def now_timestamp():
    timestamp = int(time.time())
    return timestamp
