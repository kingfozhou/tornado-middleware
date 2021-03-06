from abstractions import HTTPResponse
from middleware.request_id import request_id_middleware


@request_id_middleware
async def wrapped(request):
    return HTTPResponse(
        status_code=200,
        headers={'Content-Type': 'application/json', 'Foo': 'bar'},
        body=b'{"foo": "bar"}')
