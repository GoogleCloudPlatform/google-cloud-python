
transport inheritance structure
_______________________________

``BackendServicesTransport`` is the ABC for all transports.

- public child ``BackendServicesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BackendServicesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBackendServicesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BackendServicesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
