# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import lab2_pb2 as lab2__pb2


class BombStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMap = channel.unary_unary(
                '/lab2.Bomb/GetMap',
                request_serializer=lab2__pb2.GetMapRequest.SerializeToString,
                response_deserializer=lab2__pb2.GetMapReply.FromString,
                )


class BombServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMap(self, request, context):
        """Unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BombServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMap': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMap,
                    request_deserializer=lab2__pb2.GetMapRequest.FromString,
                    response_serializer=lab2__pb2.GetMapReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'lab2.Bomb', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bomb(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lab2.Bomb/GetMap',
            lab2__pb2.GetMapRequest.SerializeToString,
            lab2__pb2.GetMapReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class RoverMovesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMoves = channel.unary_unary(
                '/lab2.RoverMoves/GetMoves',
                request_serializer=lab2__pb2.GetRoverMoves.SerializeToString,
                response_deserializer=lab2__pb2.ReturnRoverMoves.FromString,
                )


class RoverMovesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMoves(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoverMovesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMoves': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMoves,
                    request_deserializer=lab2__pb2.GetRoverMoves.FromString,
                    response_serializer=lab2__pb2.ReturnRoverMoves.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'lab2.RoverMoves', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RoverMoves(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMoves(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lab2.RoverMoves/GetMoves',
            lab2__pb2.GetRoverMoves.SerializeToString,
            lab2__pb2.ReturnRoverMoves.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SerialNumberStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSerialNum = channel.unary_unary(
                '/lab2.SerialNumber/GetSerialNum',
                request_serializer=lab2__pb2.SerialNumReq.SerializeToString,
                response_deserializer=lab2__pb2.SerialNumReply.FromString,
                )


class SerialNumberServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSerialNum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SerialNumberServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSerialNum': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSerialNum,
                    request_deserializer=lab2__pb2.SerialNumReq.FromString,
                    response_serializer=lab2__pb2.SerialNumReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'lab2.SerialNumber', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SerialNumber(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSerialNum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lab2.SerialNumber/GetSerialNum',
            lab2__pb2.SerialNumReq.SerializeToString,
            lab2__pb2.SerialNumReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)