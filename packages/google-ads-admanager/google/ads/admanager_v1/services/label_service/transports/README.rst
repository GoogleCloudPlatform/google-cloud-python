
transport inheritance structure
_______________________________

``LabelServiceTransport`` is the ABC for all transports.

- public child ``LabelServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``LabelServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseLabelServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``LabelServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
