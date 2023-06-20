from flask import json, Response

from src.utils.json_util import CustomJsonEncoder
class ResponseResult:
    def __init__(
            self,
            data: object,
            status: int,
            code: str,
            message: str = None,
            description: object = None,
            version: str = "v1.0.0",
            pagination: {} = None
    ):
        self.data = data
        self.status = status
        self.code = code
        self.message = message
        self.description = description
        self.version = version
        self.pagination = pagination


def base_result(response_result: ResponseResult):
    try:
        if response_result is None:
            raise Exception("argument can not be null")

        result = {
            "data": response_result.data,
            "status": response_result.status,
            "code": response_result.code,
            "message": response_result.message,
            "description": response_result.description,
            "version": response_result.version,
            "pagination": response_result.pagination
        }

        return Response(
            json.dumps(result, cls=CustomJsonEncoder),
            status=response_result.status,
            mimetype='application/json'
        )

    except Exception as ex:
        raise ex


def ok_result(data: object = None, code: str = None, pagination: object = None, description: object = None) -> object:
    return base_result(ResponseResult(data=data, status=200, code=code, message=None, description=description,
                                      pagination=pagination))


# Eğer bir POST isteği istemci tarafında oluşturulmuş ID içermiyorsa
# ve istenilen kayıt başarıyla oluşturulmuşsa
# sunucu 201 Created durum kodunu dönmek zorundadır.
def created_result(data: object, code: str = None, message: str = None, description: str = None):
    return base_result(ResponseResult(data=data, status=201, code=code, message=message, description=description))


# Eğer bir kayıt ekleme isteği sunucu tarafından işlenmek için alınmışsa
# ve sunucu cevap verdiği anda hala isteğin işlenme süreci devam ediyorsa,
# sunucu 202 Accepted durum kodunu dönmek zorundadır.
def accepted_result(data: object = None, code: str = None, message: str = None, description: str = None):
    return base_result(ResponseResult(data=data, status=202, code=code, message=message, description=description))


# Eğer POST işlemi, istemci tarafında oluşturulan id‘yi içeriyorsa
# ve istenilen kayıt başarıyla oluşturulmuşsa,
# sunucu ya 201 Created durum kodu ile data nesnesini dönmeli,
# ya da 204 No Content durum kodunu içeren
# ve herhangi bir JSON nesnesi/dokümanı içermeyen cevap dönmek zorundadır.
def no_content_result(code: str = None, message: str = None, description: str = None):
    return base_result(ResponseResult(data=None, status=204, code=code, message=message, description=description))


def bad_request_result(code: str = None, message: str = None, description: str = None):
    return base_result(ResponseResult(data=None, status=400, code=code, message=message, description=description))


# Api ucunda bu işlemi yapmak için login olmak zorunlu ise
# ve apiye istek yapan kullanıcı login değil ise
# bu http status ile cevap verilir.
# Örn: kullanıcının kendi bilgilerinin güncellemesi denilebilir.
def unauthorized_result(code: str = None, message: str = None, description: str = None):
    return base_result(ResponseResult(data=None, status=401, code=code, message=message, description=description))


# Kaydın oluşturulması için desteklenmeyen bir istek gönderilmişse
# sunucu 403 Forbidden durum kodunu döndürebilir.
def forbidden_result(code: str = None, message: str = None, description: str = None):
    return base_result(ResponseResult(data=None, status=403, code=code, message=message, description=description))


# Validasyon hatalarında 422 dönecektir
# sunucu 422 validation durum kodunu döndürebilir.
def validation_result(code: str = None, message: str = None, description: str = None):
    return base_result(ResponseResult(data=None, status=422, code=code, message=message, description=description))


# Eklenecek kayıt ile ilgili kaynağın bulunmadığı durumlarda,
# sunucu 404 Not Found durum kodunu döndürmelidir.
def not_found_result(code: str = None, message: str = None, description: str = None):
    return base_result(ResponseResult(data=None, status=404, code=code, message=message, description=description))


# istek yapılan api uç noktası, gönderilen methodu implemente etmemiş ise
# bu http status unu alırız.
# Örn: login olması için token verdiğimiz bir api ucumuz var
# ve bu uçta sadece post isteğini kabul ediyor.
# Kullanıcı bu api urline GET isteği yaparsa bu hatayı alır.
def method_not_allowed_result(code: str = None, message: str = None, description: str = None):
    return base_result(ResponseResult(data=None, status=405, code=code, message=message, description=description))


# İstemci taraflı oluşturulan id halihazırda bulunuyorsa,
# sunucu 409 Conflict durum kodunu döndürmek zorundadır.
def conflict_result(code: str = None, message: str = None, description: str = None):
    return base_result(ResponseResult(data=None, status=409, code=code, message=message, description=description))


# saatlik ya da dakikaklık kısıtlanan sınırdan fazla istek yaparsak bu http statusunu alırız.
def too_many_requests_result(code: str = None, message: str = None, description: str = None):
    return base_result(ResponseResult(data=None, status=429, code=code, message=message, description=description))


# 500 hataları statusü
def internal_server_error_result(code: str = None, message: str = None, description: str = None):
    return base_result(ResponseResult(data=None, status=500, code=code, message=message, description=description))


# file tipi response döneceksek bu method ile döneriz
def file_result(data, mimetype, headers):
    return Response(data, mimetype=mimetype, headers=headers)