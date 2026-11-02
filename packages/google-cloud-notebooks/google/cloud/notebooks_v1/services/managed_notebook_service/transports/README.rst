
transport inheritance structure
_______________________________

``ManagedNotebookServiceTransport`` is the ABC for all transports.

- public child ``ManagedNotebookServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ManagedNotebookServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseManagedNotebookServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ManagedNotebookServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
