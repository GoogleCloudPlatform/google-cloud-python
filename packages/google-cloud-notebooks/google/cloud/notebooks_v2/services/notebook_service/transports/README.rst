
transport inheritance structure
_______________________________

``NotebookServiceTransport`` is the ABC for all transports.

- public child ``NotebookServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NotebookServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNotebookServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NotebookServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
