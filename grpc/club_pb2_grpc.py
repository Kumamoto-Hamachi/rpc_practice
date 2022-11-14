# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import club_pb2 as club__pb2


class ClubManagerStub(object):
    """クラブ管理を行うサービス
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetClub = channel.unary_unary(
                '/ClubManager/GetClub',
                request_serializer=club__pb2.ClubRequest.SerializeToString,
                response_deserializer=club__pb2.ClubResponse.FromString,
                )


class ClubManagerServicer(object):
    """クラブ管理を行うサービス
    """

    def GetClub(self, request, context):
        """クラブ情報を取得する
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClubManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetClub': grpc.unary_unary_rpc_method_handler(
                    servicer.GetClub,
                    request_deserializer=club__pb2.ClubRequest.FromString,
                    response_serializer=club__pb2.ClubResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ClubManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClubManager(object):
    """クラブ管理を行うサービス
    """

    @staticmethod
    def GetClub(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClubManager/GetClub',
            club__pb2.ClubRequest.SerializeToString,
            club__pb2.ClubResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
