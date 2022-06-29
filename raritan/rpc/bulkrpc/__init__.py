# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/gitlab/builds/1da4124e/0/gitlab/main/firmware/mkdist/tmp/build-pdu-px2-final/jsonrpcd/src/idl/BulkRequest.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
from raritan.rpc.opaque.bulkrpc import JsonObject

import raritan.rpc.bulkrpc


# structure
class Request(Structure):
    idlType = "bulkrpc.Request:1.0.0"
    elements = ["rid", "json"]

    def __init__(self, rid, json):
        typecheck.is_string(rid, AssertionError)
        typecheck.is_string(json, AssertionError)

        self.rid = rid
        self.json = json

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            rid = json['rid'],
            json = json['json'],
        )
        return obj

    def encode(self):
        json = {}
        json['rid'] = self.rid
        json['json'] = self.json
        return json

# structure
class Response(Structure):
    idlType = "bulkrpc.Response:1.0.0"
    elements = ["json", "statcode"]

    def __init__(self, json, statcode):
        typecheck.is_string(json, AssertionError)
        typecheck.is_int(statcode, AssertionError)

        self.json = json
        self.statcode = statcode

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            json = json['json'],
            statcode = json['statcode'],
        )
        return obj

    def encode(self):
        json = {}
        json['json'] = self.json
        json['statcode'] = self.statcode
        return json

# interface
class BulkRequest(Interface):
    idlType = "bulkrpc.BulkRequest:1.0.2"

    # structure
    class Request(Structure):
        idlType = "bulkrpc.BulkRequest_1_0_2.Request:1.0.0"
        elements = ["rid", "json"]

        def __init__(self, rid, json):
            typecheck.is_string(rid, AssertionError)

            self.rid = rid
            self.json = json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                rid = json['rid'],
                json = raritan.rpc.bulkrpc.JsonObject.decode(json['json'], agent),
            )
            return obj

        def encode(self):
            json = {}
            json['rid'] = self.rid
            json['json'] = raritan.rpc.bulkrpc.JsonObject.encode(self.json)
            return json

    # structure
    class Response(Structure):
        idlType = "bulkrpc.BulkRequest_1_0_2.Response:1.0.0"
        elements = ["json", "statcode"]

        def __init__(self, json, statcode):
            typecheck.is_int(statcode, AssertionError)

            self.json = json
            self.statcode = statcode

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                json = raritan.rpc.bulkrpc.JsonObject.decode(json['json'], agent),
                statcode = json['statcode'],
            )
            return obj

        def encode(self):
            json = {}
            json['json'] = raritan.rpc.bulkrpc.JsonObject.encode(self.json)
            json['statcode'] = self.statcode
            return json

    class _performRequest(Interface.Method):
        name = 'performRequest'

        @staticmethod
        def encode(requests):
            for x0 in requests:
                typecheck.is_struct(x0, raritan.rpc.bulkrpc.Request, AssertionError)
            args = {}
            args['requests'] = [raritan.rpc.bulkrpc.Request.encode(x0) for x0 in requests]
            return args

        @staticmethod
        def decode(rsp, agent):
            responses = [raritan.rpc.bulkrpc.Response.decode(x0, agent) for x0 in rsp['responses']]
            for x0 in responses:
                typecheck.is_struct(x0, raritan.rpc.bulkrpc.Response, DecodeException)
            return responses

    class _performBulk(Interface.Method):
        name = 'performBulk'

        @staticmethod
        def encode(requests):
            for x0 in requests:
                typecheck.is_struct(x0, raritan.rpc.bulkrpc.BulkRequest.Request, AssertionError)
            args = {}
            args['requests'] = [raritan.rpc.bulkrpc.BulkRequest.Request.encode(x0) for x0 in requests]
            return args

        @staticmethod
        def decode(rsp, agent):
            responses = [raritan.rpc.bulkrpc.BulkRequest.Response.decode(x0, agent) for x0 in rsp['responses']]
            for x0 in responses:
                typecheck.is_struct(x0, raritan.rpc.bulkrpc.BulkRequest.Response, DecodeException)
            return responses

    class _performBulkTimeout(Interface.Method):
        name = 'performBulkTimeout'

        @staticmethod
        def encode(requests, timeoutMs):
            for x0 in requests:
                typecheck.is_struct(x0, raritan.rpc.bulkrpc.BulkRequest.Request, AssertionError)
            typecheck.is_int(timeoutMs, AssertionError)
            args = {}
            args['requests'] = [raritan.rpc.bulkrpc.BulkRequest.Request.encode(x0) for x0 in requests]
            args['timeoutMs'] = timeoutMs
            return args

        @staticmethod
        def decode(rsp, agent):
            responses = [raritan.rpc.bulkrpc.BulkRequest.Response.decode(x0, agent) for x0 in rsp['responses']]
            for x0 in responses:
                typecheck.is_struct(x0, raritan.rpc.bulkrpc.BulkRequest.Response, DecodeException)
            return responses
    def __init__(self, target, agent):
        super(BulkRequest, self).__init__(target, agent)
        self.performRequest = BulkRequest._performRequest(self)
        self.performBulk = BulkRequest._performBulk(self)
        self.performBulkTimeout = BulkRequest._performBulkTimeout(self)