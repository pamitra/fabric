import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
import peer.admin_pb2 as peer_dot_admin__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
import peer.admin_pb2 as peer_dot_admin__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
import peer.admin_pb2 as peer_dot_admin__pb2
import peer.admin_pb2 as peer_dot_admin__pb2
import peer.admin_pb2 as peer_dot_admin__pb2
import peer.admin_pb2 as peer_dot_admin__pb2
import peer.admin_pb2 as peer_dot_admin__pb2


class AdminStub(object):
  """Interface exported by the server.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetStatus = channel.unary_unary(
        '/protos.Admin/GetStatus',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=peer_dot_admin__pb2.ServerStatus.FromString,
        )
    self.StartServer = channel.unary_unary(
        '/protos.Admin/StartServer',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=peer_dot_admin__pb2.ServerStatus.FromString,
        )
    self.StopServer = channel.unary_unary(
        '/protos.Admin/StopServer',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=peer_dot_admin__pb2.ServerStatus.FromString,
        )
    self.GetModuleLogLevel = channel.unary_unary(
        '/protos.Admin/GetModuleLogLevel',
        request_serializer=peer_dot_admin__pb2.LogLevelRequest.SerializeToString,
        response_deserializer=peer_dot_admin__pb2.LogLevelResponse.FromString,
        )
    self.SetModuleLogLevel = channel.unary_unary(
        '/protos.Admin/SetModuleLogLevel',
        request_serializer=peer_dot_admin__pb2.LogLevelRequest.SerializeToString,
        response_deserializer=peer_dot_admin__pb2.LogLevelResponse.FromString,
        )


class AdminServicer(object):
  """Interface exported by the server.
  """

  def GetStatus(self, request, context):
    """Return the serve status.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartServer(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopServer(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetModuleLogLevel(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetModuleLogLevel(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdminServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetStatus,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=peer_dot_admin__pb2.ServerStatus.SerializeToString,
      ),
      'StartServer': grpc.unary_unary_rpc_method_handler(
          servicer.StartServer,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=peer_dot_admin__pb2.ServerStatus.SerializeToString,
      ),
      'StopServer': grpc.unary_unary_rpc_method_handler(
          servicer.StopServer,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=peer_dot_admin__pb2.ServerStatus.SerializeToString,
      ),
      'GetModuleLogLevel': grpc.unary_unary_rpc_method_handler(
          servicer.GetModuleLogLevel,
          request_deserializer=peer_dot_admin__pb2.LogLevelRequest.FromString,
          response_serializer=peer_dot_admin__pb2.LogLevelResponse.SerializeToString,
      ),
      'SetModuleLogLevel': grpc.unary_unary_rpc_method_handler(
          servicer.SetModuleLogLevel,
          request_deserializer=peer_dot_admin__pb2.LogLevelRequest.FromString,
          response_serializer=peer_dot_admin__pb2.LogLevelResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protos.Admin', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
