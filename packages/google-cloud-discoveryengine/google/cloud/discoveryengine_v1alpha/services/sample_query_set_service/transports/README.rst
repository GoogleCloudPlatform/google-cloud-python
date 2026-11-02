
transport inheritance structure
_______________________________

``SampleQuerySetServiceTransport`` is the ABC for all transports.

- public child ``SampleQuerySetServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SampleQuerySetServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSampleQuerySetServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SampleQuerySetServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
