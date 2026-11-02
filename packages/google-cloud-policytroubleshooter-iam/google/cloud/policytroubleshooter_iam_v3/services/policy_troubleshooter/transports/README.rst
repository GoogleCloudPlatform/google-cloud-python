
transport inheritance structure
_______________________________

``PolicyTroubleshooterTransport`` is the ABC for all transports.

- public child ``PolicyTroubleshooterGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PolicyTroubleshooterGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePolicyTroubleshooterRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PolicyTroubleshooterRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
