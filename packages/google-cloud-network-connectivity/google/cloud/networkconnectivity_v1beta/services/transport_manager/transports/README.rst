
transport inheritance structure
_______________________________

``TransportManagerTransport`` is the ABC for all transports.

- public child ``TransportManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TransportManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTransportManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TransportManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
