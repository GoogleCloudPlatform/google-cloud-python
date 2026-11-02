
transport inheritance structure
_______________________________

``AccountServicesServiceTransport`` is the ABC for all transports.

- public child ``AccountServicesServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AccountServicesServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAccountServicesServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AccountServicesServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
