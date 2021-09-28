# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import location_pb2 as location__pb2


class LocationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateLocation = channel.unary_unary(
                '/LocationService/CreateLocation',
                request_serializer=location__pb2.CreateLocationRequest.SerializeToString,
                response_deserializer=location__pb2.CreateLocationResponse.FromString,
                )
        self.GetLocation = channel.unary_unary(
                '/LocationService/GetLocation',
                request_serializer=location__pb2.GetLocationRequest.SerializeToString,
                response_deserializer=location__pb2.Location.FromString,
                )
        self.ListExposedLocations = channel.unary_unary(
                '/LocationService/ListExposedLocations',
                request_serializer=location__pb2.ListExposedLocationsRequest.SerializeToString,
                response_deserializer=location__pb2.ListExposedLocationsResponse.FromString,
                )


class LocationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateLocation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLocation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExposedLocations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LocationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateLocation,
                    request_deserializer=location__pb2.CreateLocationRequest.FromString,
                    response_serializer=location__pb2.CreateLocationResponse.SerializeToString,
            ),
            'GetLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLocation,
                    request_deserializer=location__pb2.GetLocationRequest.FromString,
                    response_serializer=location__pb2.Location.SerializeToString,
            ),
            'ListExposedLocations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExposedLocations,
                    request_deserializer=location__pb2.ListExposedLocationsRequest.FromString,
                    response_serializer=location__pb2.ListExposedLocationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LocationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LocationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LocationService/CreateLocation',
            location__pb2.CreateLocationRequest.SerializeToString,
            location__pb2.CreateLocationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LocationService/GetLocation',
            location__pb2.GetLocationRequest.SerializeToString,
            location__pb2.Location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListExposedLocations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LocationService/ListExposedLocations',
            location__pb2.ListExposedLocationsRequest.SerializeToString,
            location__pb2.ListExposedLocationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)