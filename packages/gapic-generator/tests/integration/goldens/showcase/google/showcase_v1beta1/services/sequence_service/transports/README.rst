
transport inheritance structure
_______________________________

``SequenceServiceTransport`` is the ABC for all transports.

- public child ``SequenceServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SequenceServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSequenceServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SequenceServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
