
transport inheritance structure
_______________________________

``RoutesTransport`` is the ABC for all transports.

- public child ``RoutesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RoutesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRoutesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RoutesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
