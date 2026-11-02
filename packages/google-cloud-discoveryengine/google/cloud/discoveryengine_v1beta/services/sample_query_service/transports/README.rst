
transport inheritance structure
_______________________________

``SampleQueryServiceTransport`` is the ABC for all transports.

- public child ``SampleQueryServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SampleQueryServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSampleQueryServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SampleQueryServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
