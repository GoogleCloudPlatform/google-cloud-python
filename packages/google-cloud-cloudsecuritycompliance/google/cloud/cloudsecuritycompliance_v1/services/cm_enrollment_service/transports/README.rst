
transport inheritance structure
_______________________________

``CmEnrollmentServiceTransport`` is the ABC for all transports.

- public child ``CmEnrollmentServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CmEnrollmentServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCmEnrollmentServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CmEnrollmentServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
