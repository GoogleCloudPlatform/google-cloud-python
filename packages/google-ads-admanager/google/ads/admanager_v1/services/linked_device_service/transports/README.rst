
transport inheritance structure
_______________________________

``LinkedDeviceServiceTransport`` is the ABC for all transports.

- public child ``LinkedDeviceServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LinkedDeviceServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLinkedDeviceServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LinkedDeviceServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
