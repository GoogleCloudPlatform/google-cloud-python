
transport inheritance structure
_______________________________

``BuildsTransport`` is the ABC for all transports.

- public child ``BuildsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BuildsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBuildsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BuildsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
