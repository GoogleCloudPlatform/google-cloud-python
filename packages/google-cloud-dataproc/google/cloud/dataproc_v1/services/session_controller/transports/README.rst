
transport inheritance structure
_______________________________

``SessionControllerTransport`` is the ABC for all transports.

- public child ``SessionControllerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SessionControllerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSessionControllerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SessionControllerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
