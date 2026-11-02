
transport inheritance structure
_______________________________

``RegistrationServiceTransport`` is the ABC for all transports.

- public child ``RegistrationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RegistrationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRegistrationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RegistrationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
