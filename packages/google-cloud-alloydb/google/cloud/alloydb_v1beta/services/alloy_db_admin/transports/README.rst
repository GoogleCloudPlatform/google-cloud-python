
transport inheritance structure
_______________________________

``AlloyDBAdminTransport`` is the ABC for all transports.

- public child ``AlloyDBAdminGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AlloyDBAdminGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAlloyDBAdminRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AlloyDBAdminRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
