
transport inheritance structure
_______________________________

``ChangeEventServiceTransport`` is the ABC for all transports.

- public child ``ChangeEventServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ChangeEventServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseChangeEventServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ChangeEventServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
