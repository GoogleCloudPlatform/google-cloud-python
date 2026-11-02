
transport inheritance structure
_______________________________

``BusinessGlossaryServiceTransport`` is the ABC for all transports.

- public child ``BusinessGlossaryServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BusinessGlossaryServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBusinessGlossaryServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BusinessGlossaryServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
