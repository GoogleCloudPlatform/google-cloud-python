
transport inheritance structure
_______________________________

``PagesTransport`` is the ABC for all transports.

- public child ``PagesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PagesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePagesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PagesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
