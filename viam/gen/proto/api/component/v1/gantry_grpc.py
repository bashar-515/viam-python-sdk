import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ..... import proto

class GantryServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[proto.api.component.v1.gantry_pb2.GantryServiceGetPositionRequest, proto.api.component.v1.gantry_pb2.GantryServiceGetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveToPosition(self, stream: 'grpclib.server.Stream[proto.api.component.v1.gantry_pb2.GantryServiceMoveToPositionRequest, proto.api.component.v1.gantry_pb2.GantryServiceMoveToPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetLengths(self, stream: 'grpclib.server.Stream[proto.api.component.v1.gantry_pb2.GantryServiceGetLengthsRequest, proto.api.component.v1.gantry_pb2.GantryServiceGetLengthsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.GantryService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.gantry_pb2.GantryServiceGetPositionRequest, proto.api.component.v1.gantry_pb2.GantryServiceGetPositionResponse), '/proto.api.component.v1.GantryService/MoveToPosition': grpclib.const.Handler(self.MoveToPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.gantry_pb2.GantryServiceMoveToPositionRequest, proto.api.component.v1.gantry_pb2.GantryServiceMoveToPositionResponse), '/proto.api.component.v1.GantryService/GetLengths': grpclib.const.Handler(self.GetLengths, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.gantry_pb2.GantryServiceGetLengthsRequest, proto.api.component.v1.gantry_pb2.GantryServiceGetLengthsResponse)}

class GantryServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.GantryService/GetPosition', proto.api.component.v1.gantry_pb2.GantryServiceGetPositionRequest, proto.api.component.v1.gantry_pb2.GantryServiceGetPositionResponse)
        self.MoveToPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.GantryService/MoveToPosition', proto.api.component.v1.gantry_pb2.GantryServiceMoveToPositionRequest, proto.api.component.v1.gantry_pb2.GantryServiceMoveToPositionResponse)
        self.GetLengths = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.GantryService/GetLengths', proto.api.component.v1.gantry_pb2.GantryServiceGetLengthsRequest, proto.api.component.v1.gantry_pb2.GantryServiceGetLengthsResponse)