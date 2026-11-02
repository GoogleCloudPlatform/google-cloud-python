
transport inheritance structure
_______________________________

``OrderTrackingSignalsServiceTransport`` is the ABC for all transports.

- public child ``OrderTrackingSignalsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``OrderTrackingSignalsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseOrderTrackingSignalsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``OrderTrackingSignalsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
