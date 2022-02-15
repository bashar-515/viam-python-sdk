import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ..... import proto

class BaseServiceBase(abc.ABC):

    @abc.abstractmethod
    async def MoveStraight(self, stream: 'grpclib.server.Stream[proto.api.component.v1.base_pb2.BaseServiceMoveStraightRequest, proto.api.component.v1.base_pb2.BaseServiceMoveStraightResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveArc(self, stream: 'grpclib.server.Stream[proto.api.component.v1.base_pb2.BaseServiceMoveArcRequest, proto.api.component.v1.base_pb2.BaseServiceMoveArcResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Spin(self, stream: 'grpclib.server.Stream[proto.api.component.v1.base_pb2.BaseServiceSpinRequest, proto.api.component.v1.base_pb2.BaseServiceSpinResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[proto.api.component.v1.base_pb2.BaseServiceStopRequest, proto.api.component.v1.base_pb2.BaseServiceStopResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.BaseService/MoveStraight': grpclib.const.Handler(self.MoveStraight, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.base_pb2.BaseServiceMoveStraightRequest, proto.api.component.v1.base_pb2.BaseServiceMoveStraightResponse), '/proto.api.component.v1.BaseService/MoveArc': grpclib.const.Handler(self.MoveArc, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.base_pb2.BaseServiceMoveArcRequest, proto.api.component.v1.base_pb2.BaseServiceMoveArcResponse), '/proto.api.component.v1.BaseService/Spin': grpclib.const.Handler(self.Spin, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.base_pb2.BaseServiceSpinRequest, proto.api.component.v1.base_pb2.BaseServiceSpinResponse), '/proto.api.component.v1.BaseService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.base_pb2.BaseServiceStopRequest, proto.api.component.v1.base_pb2.BaseServiceStopResponse)}

class BaseServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.MoveStraight = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.BaseService/MoveStraight', proto.api.component.v1.base_pb2.BaseServiceMoveStraightRequest, proto.api.component.v1.base_pb2.BaseServiceMoveStraightResponse)
        self.MoveArc = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.BaseService/MoveArc', proto.api.component.v1.base_pb2.BaseServiceMoveArcRequest, proto.api.component.v1.base_pb2.BaseServiceMoveArcResponse)
        self.Spin = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.BaseService/Spin', proto.api.component.v1.base_pb2.BaseServiceSpinRequest, proto.api.component.v1.base_pb2.BaseServiceSpinResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.BaseService/Stop', proto.api.component.v1.base_pb2.BaseServiceStopRequest, proto.api.component.v1.base_pb2.BaseServiceStopResponse)