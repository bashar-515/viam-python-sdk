"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
from .... import common
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MoveRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DESTINATION_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    WORLD_STATE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def destination(self) -> common.v1.common_pb2.PoseInFrame:
        ...

    @property
    def component_name(self) -> common.v1.common_pb2.ResourceName:
        ...

    @property
    def world_state(self) -> common.v1.common_pb2.WorldState:
        ...

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., destination: common.v1.common_pb2.PoseInFrame | None=..., component_name: common.v1.common_pb2.ResourceName | None=..., world_state: common.v1.common_pb2.WorldState | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_world_state', b'_world_state', 'component_name', b'component_name', 'destination', b'destination', 'extra', b'extra', 'world_state', b'world_state']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_world_state', b'_world_state', 'component_name', b'component_name', 'destination', b'destination', 'extra', b'extra', 'name', b'name', 'world_state', b'world_state']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_world_state', b'_world_state']) -> typing_extensions.Literal['world_state'] | None:
        ...
global___MoveRequest = MoveRequest

class MoveResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUCCESS_FIELD_NUMBER: builtins.int
    success: builtins.bool

    def __init__(self, *, success: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['success', b'success']) -> None:
        ...
global___MoveResponse = MoveResponse

class MoveSingleComponentRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DESTINATION_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    WORLD_STATE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def destination(self) -> common.v1.common_pb2.PoseInFrame:
        ...

    @property
    def component_name(self) -> common.v1.common_pb2.ResourceName:
        ...

    @property
    def world_state(self) -> common.v1.common_pb2.WorldState:
        ...

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., destination: common.v1.common_pb2.PoseInFrame | None=..., component_name: common.v1.common_pb2.ResourceName | None=..., world_state: common.v1.common_pb2.WorldState | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_world_state', b'_world_state', 'component_name', b'component_name', 'destination', b'destination', 'extra', b'extra', 'world_state', b'world_state']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_world_state', b'_world_state', 'component_name', b'component_name', 'destination', b'destination', 'extra', b'extra', 'name', b'name', 'world_state', b'world_state']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_world_state', b'_world_state']) -> typing_extensions.Literal['world_state'] | None:
        ...
global___MoveSingleComponentRequest = MoveSingleComponentRequest

class MoveSingleComponentResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUCCESS_FIELD_NUMBER: builtins.int
    success: builtins.bool

    def __init__(self, *, success: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['success', b'success']) -> None:
        ...
global___MoveSingleComponentResponse = MoveSingleComponentResponse

class GetPoseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    DESTINATION_FRAME_FIELD_NUMBER: builtins.int
    SUPPLEMENTAL_TRANSFORMS_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def component_name(self) -> common.v1.common_pb2.ResourceName:
        """the component whose pose is being requested"""
    destination_frame: builtins.str
    'the reference frame in which the component\'s pose\n    should be provided, if unset this defaults\n    to the "world" reference frame\n    '

    @property
    def supplemental_transforms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.v1.common_pb2.Transform]:
        """pose information on any additional reference frames that are needed
        to compute the component's pose
        """

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., component_name: common.v1.common_pb2.ResourceName | None=..., destination_frame: builtins.str=..., supplemental_transforms: collections.abc.Iterable[common.v1.common_pb2.Transform] | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['component_name', b'component_name', 'extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['component_name', b'component_name', 'destination_frame', b'destination_frame', 'extra', b'extra', 'name', b'name', 'supplemental_transforms', b'supplemental_transforms']) -> None:
        ...
global___GetPoseRequest = GetPoseRequest

class GetPoseResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSE_FIELD_NUMBER: builtins.int

    @property
    def pose(self) -> common.v1.common_pb2.PoseInFrame:
        ...

    def __init__(self, *, pose: common.v1.common_pb2.PoseInFrame | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> None:
        ...
global___GetPoseResponse = GetPoseResponse