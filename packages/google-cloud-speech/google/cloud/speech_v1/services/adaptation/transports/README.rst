
transport inheritance structure
_______________________________

``AdaptationTransport`` is the ABC for all transports.

- public child ``AdaptationGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AdaptationGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAdaptationRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AdaptationRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
