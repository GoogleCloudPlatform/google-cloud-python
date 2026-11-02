
transport inheritance structure
_______________________________

``DeviceManufacturerServiceTransport`` is the ABC for all transports.

- public child ``DeviceManufacturerServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DeviceManufacturerServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDeviceManufacturerServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DeviceManufacturerServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
