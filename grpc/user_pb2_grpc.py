# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import user_pb2 as user__pb2


class UserManagerStub(object):
    """ユーザー管理を行うサービス
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUser = channel.unary_unary(
                '/UserManager/GetUser',
                request_serializer=user__pb2.UserRequest.SerializeToString,
                response_deserializer=user__pb2.UserResponse.FromString,
                )
        self.AddUser = channel.unary_unary(
                '/UserManager/AddUser',
                request_serializer=user__pb2.User.SerializeToString,
                response_deserializer=user__pb2.UserResponse.FromString,
                )
        self.CountAlreadyUsers = channel.stream_unary(
                '/UserManager/CountAlreadyUsers',
                request_serializer=user__pb2.UserRequest.SerializeToString,
                response_deserializer=user__pb2.UserCntResponse.FromString,
                )
        self.GetUsersByType = channel.unary_stream(
                '/UserManager/GetUsersByType',
                request_serializer=user__pb2.UserTypeRequest.SerializeToString,
                response_deserializer=user__pb2.UserResponse.FromString,
                )
        self.GetUsersByIds = channel.stream_stream(
                '/UserManager/GetUsersByIds',
                request_serializer=user__pb2.UserRequest.SerializeToString,
                response_deserializer=user__pb2.UserResponse.FromString,
                )


class UserManagerServicer(object):
    """ユーザー管理を行うサービス
    """

    def GetUser(self, request, context):
        """ユーザー情報を取得する
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUser(self, request, context):
        """新規のユーザー情報を追加する
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CountAlreadyUsers(self, request_iterator, context):
        """与えられたユーザーのうち存在する人数を取得する
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsersByType(self, request, context):
        """与えられたユーザータイプと同種のユーザーを取得する
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsersByIds(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=user__pb2.UserRequest.FromString,
                    response_serializer=user__pb2.UserResponse.SerializeToString,
            ),
            'AddUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUser,
                    request_deserializer=user__pb2.User.FromString,
                    response_serializer=user__pb2.UserResponse.SerializeToString,
            ),
            'CountAlreadyUsers': grpc.stream_unary_rpc_method_handler(
                    servicer.CountAlreadyUsers,
                    request_deserializer=user__pb2.UserRequest.FromString,
                    response_serializer=user__pb2.UserCntResponse.SerializeToString,
            ),
            'GetUsersByType': grpc.unary_stream_rpc_method_handler(
                    servicer.GetUsersByType,
                    request_deserializer=user__pb2.UserTypeRequest.FromString,
                    response_serializer=user__pb2.UserResponse.SerializeToString,
            ),
            'GetUsersByIds': grpc.stream_stream_rpc_method_handler(
                    servicer.GetUsersByIds,
                    request_deserializer=user__pb2.UserRequest.FromString,
                    response_serializer=user__pb2.UserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UserManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserManager(object):
    """ユーザー管理を行うサービス
    """

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserManager/GetUser',
            user__pb2.UserRequest.SerializeToString,
            user__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserManager/AddUser',
            user__pb2.User.SerializeToString,
            user__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CountAlreadyUsers(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/UserManager/CountAlreadyUsers',
            user__pb2.UserRequest.SerializeToString,
            user__pb2.UserCntResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsersByType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/UserManager/GetUsersByType',
            user__pb2.UserTypeRequest.SerializeToString,
            user__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsersByIds(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/UserManager/GetUsersByIds',
            user__pb2.UserRequest.SerializeToString,
            user__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
