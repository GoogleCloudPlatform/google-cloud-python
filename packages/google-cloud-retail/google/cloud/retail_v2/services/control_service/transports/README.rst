
transport inheritance structure
_______________________________

``ControlServiceTransport`` is the ABC for all transports.

- public child ``ControlServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ControlServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseControlServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ControlServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
