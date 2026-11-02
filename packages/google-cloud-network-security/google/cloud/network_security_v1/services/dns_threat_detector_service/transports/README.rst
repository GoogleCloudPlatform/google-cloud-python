
transport inheritance structure
_______________________________

``DnsThreatDetectorServiceTransport`` is the ABC for all transports.

- public child ``DnsThreatDetectorServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DnsThreatDetectorServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDnsThreatDetectorServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DnsThreatDetectorServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
