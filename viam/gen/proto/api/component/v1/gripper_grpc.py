import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ..... import proto

class GripperServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Open(self, stream: 'grpclib.server.Stream[proto.api.component.v1.gripper_pb2.GripperServiceOpenRequest, proto.api.component.v1.gripper_pb2.GripperServiceOpenResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Grab(self, stream: 'grpclib.server.Stream[proto.api.component.v1.gripper_pb2.GripperServiceGrabRequest, proto.api.component.v1.gripper_pb2.GripperServiceGrabResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.GripperService/Open': grpclib.const.Handler(self.Open, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.gripper_pb2.GripperServiceOpenRequest, proto.api.component.v1.gripper_pb2.GripperServiceOpenResponse), '/proto.api.component.v1.GripperService/Grab': grpclib.const.Handler(self.Grab, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.gripper_pb2.GripperServiceGrabRequest, proto.api.component.v1.gripper_pb2.GripperServiceGrabResponse)}

class GripperServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Open = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.GripperService/Open', proto.api.component.v1.gripper_pb2.GripperServiceOpenRequest, proto.api.component.v1.gripper_pb2.GripperServiceOpenResponse)
        self.Grab = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.GripperService/Grab', proto.api.component.v1.gripper_pb2.GripperServiceGrabRequest, proto.api.component.v1.gripper_pb2.GripperServiceGrabResponse)