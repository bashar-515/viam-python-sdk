import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.struct_pb2
import google.api.annotations_pb2
from ..... import proto

class SensorServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetReadings(self, stream: 'grpclib.server.Stream[proto.api.component.v1.sensor_pb2.SensorServiceGetReadingsRequest, proto.api.component.v1.sensor_pb2.SensorServiceGetReadingsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.SensorService/GetReadings': grpclib.const.Handler(self.GetReadings, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.sensor_pb2.SensorServiceGetReadingsRequest, proto.api.component.v1.sensor_pb2.SensorServiceGetReadingsResponse)}

class SensorServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetReadings = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.SensorService/GetReadings', proto.api.component.v1.sensor_pb2.SensorServiceGetReadingsRequest, proto.api.component.v1.sensor_pb2.SensorServiceGetReadingsResponse)