
transport inheritance structure
_______________________________

``GlobalFolderOperationsTransport`` is the ABC for all transports.

- public child ``GlobalFolderOperationsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GlobalFolderOperationsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGlobalFolderOperationsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GlobalFolderOperationsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
