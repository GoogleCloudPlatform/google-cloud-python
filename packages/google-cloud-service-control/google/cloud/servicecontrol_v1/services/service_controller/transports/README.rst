
transport inheritance structure
_______________________________

``ServiceControllerTransport`` is the ABC for all transports.

- public child ``ServiceControllerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ServiceControllerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseServiceControllerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ServiceControllerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
