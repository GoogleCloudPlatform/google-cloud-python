
transport inheritance structure
_______________________________

``ZoneFolderOperationsTransport`` is the ABC for all transports.

- public child ``ZoneFolderOperationsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ZoneFolderOperationsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseZoneFolderOperationsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ZoneFolderOperationsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
