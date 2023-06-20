import datetime
import decimal

import bson
from bson import ObjectId
from flask import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from bson.json_util import dumps, loads


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        elif isinstance(obj, ObjectId):
            return str(obj)

        elif isinstance(obj.__class__, DeclarativeMeta):
            data = {}
            fields = obj.__json__() if hasattr(obj, '__json__') else dir(obj)
            for field in [f for f in fields if not f.startswith('_') and f not in ['metadata', 'query', 'query_class']]:
                value = obj.__getattribute__(field)
                try:
                    json.dumps(value)
                    data[field] = value
                except TypeError:
                    data[field] = None
            return data
        elif isinstance(obj, decimal.Decimal):
            return str(obj)
        elif isinstance(obj, bson.objectid.ObjectId):
            return str(obj)

        return json.JSONEncoder.default(self, obj)


def json_decoder(obj):
    return obj


# Encoder function
def json_dumps(obj):
    return json.dumps(obj, cls=CustomJsonEncoder)


# Decoder function
def json_loads(obj):
    return json.loads(obj, object_hook=json_decoder)


def is_jsonable(obj):
    try:
        json.dumps(obj)
        return True
    except (TypeError, OverflowError):
        return False


def list_to_string(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += "'" + ele + "',"

        # return string
    return str1.rstrip(',')
