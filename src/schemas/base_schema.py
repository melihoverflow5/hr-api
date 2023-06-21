from datetime import date
from pprint import pprint
from flask import request
from marshmallow import Schema, fields

default_error_messages = {
    "null": "alan boş olamaz",
    "required": "alan gereklidir",
    "validator_failed": "doğrulanamayan değer",
    "invalid": "alan verisi hatalı",
    "default_message": "doğrulanamayan değer"
}


class BaseSchema(Schema):
    def __init__(self, many: bool = False, *args, **kwargs):
        kwargs["many"] = many
        # kwargs["strict"] = True
        super().__init__(*args, **kwargs)

    def get_args(self):
        payload = request.args
        schema = self.deserialize(payload)
        return schema

    def get_json(self):
        payload = request.json
        schema = self.deserialize(payload)
        print(schema)
        return schema

    def deserialize(self, payload):
        """
        - Objeyi validasyon'dan geçirir ve eğer valid olmuyorsa exception atar
        - Şemadan şemaya dönüştürme yapmak için de kullanılır.
        :param payload:
        :return:
        """
        result = self.load(payload)
        return result

    def serialize(self, payload=None, many=False):
        """
        - DB'den gelen ObjectId değerlerini string'e dönüştürür.
        - UI'a gönderilirken kullanılır
        :param many:
        :param payload:
        :return:
        """
        if many:
            results = []
            for i in payload:
                item = self.serialize(i)
                results.append(item)
            return results

        result = self.dump(payload)
        return result

