
transport inheritance structure
_______________________________

``SecurityProfileGroupServiceTransport`` is the ABC for all transports.

- public child ``SecurityProfileGroupServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SecurityProfileGroupServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSecurityProfileGroupServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SecurityProfileGroupServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
