
transport inheritance structure
_______________________________

``HaControllersTransport`` is the ABC for all transports.

- public child ``HaControllersGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``HaControllersGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseHaControllersRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``HaControllersRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
