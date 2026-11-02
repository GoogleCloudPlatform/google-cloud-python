
transport inheritance structure
_______________________________

``IsochroneServiceTransport`` is the ABC for all transports.

- public child ``IsochroneServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``IsochroneServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseIsochroneServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``IsochroneServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
