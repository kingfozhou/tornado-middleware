import json

from marshmallow import fields, Schema
from tornado.httputil import HTTPServerRequest, HTTPHeaders
from tornado.testing import AsyncTestCase, gen_test

from handlers.bind_request import bind_arguments, Json, Header


class RequestFiltersSchema(Schema):
    account_id = fields.Int(required=True)


class RequestSchema(Schema):
    filters = fields.Nested(RequestFiltersSchema, required=True)
    institution_id = fields.List(fields.Int(required=True), required=True)
    message_id = fields.Str(allow_none=False)


@bind_arguments
async def foo1(request, data: RequestSchema, js: Json, message_id: Header('X-Request-Id')):
    print('request', request)
    print('data', data)
    print('json', js)
    print('message_id', message_id)


class BindArgumentsTests(AsyncTestCase):
    @gen_test
    async def test_foo(self):


        data = {
            "institution_id": ["1001"],
            "filters": {
                "account_id": "123456"
            }
        }
        request = HTTPServerRequest(uri='/', body=json.dumps(data), headers=HTTPHeaders({'X-Request-Id': 'foo'}))

        await foo1(request)
