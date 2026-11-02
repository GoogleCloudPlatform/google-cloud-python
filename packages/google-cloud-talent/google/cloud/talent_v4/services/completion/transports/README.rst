
transport inheritance structure
_______________________________

``CompletionTransport`` is the ABC for all transports.

- public child ``CompletionGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CompletionGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCompletionRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CompletionRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
