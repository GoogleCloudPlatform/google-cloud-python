
transport inheritance structure
_______________________________

``FoldersTransport`` is the ABC for all transports.

- public child ``FoldersGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FoldersGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFoldersRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FoldersRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
