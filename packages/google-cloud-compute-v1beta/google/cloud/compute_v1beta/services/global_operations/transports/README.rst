
transport inheritance structure
_______________________________

``GlobalOperationsTransport`` is the ABC for all transports.

- public child ``GlobalOperationsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GlobalOperationsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGlobalOperationsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GlobalOperationsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
