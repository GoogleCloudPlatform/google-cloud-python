
transport inheritance structure
_______________________________

``ExecutionsTransport`` is the ABC for all transports.

- public child ``ExecutionsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ExecutionsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseExecutionsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ExecutionsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
