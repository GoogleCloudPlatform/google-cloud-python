
transport inheritance structure
_______________________________

``HomepageServiceTransport`` is the ABC for all transports.

- public child ``HomepageServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``HomepageServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseHomepageServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``HomepageServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
