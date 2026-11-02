
transport inheritance structure
_______________________________

``CloudFilestoreManagerTransport`` is the ABC for all transports.

- public child ``CloudFilestoreManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudFilestoreManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudFilestoreManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudFilestoreManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
