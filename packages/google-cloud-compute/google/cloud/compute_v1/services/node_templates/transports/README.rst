
transport inheritance structure
_______________________________

``NodeTemplatesTransport`` is the ABC for all transports.

- public child ``NodeTemplatesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NodeTemplatesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNodeTemplatesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NodeTemplatesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
