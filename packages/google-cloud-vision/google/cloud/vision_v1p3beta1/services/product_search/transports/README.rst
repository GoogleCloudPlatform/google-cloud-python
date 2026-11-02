
transport inheritance structure
_______________________________

``ProductSearchTransport`` is the ABC for all transports.

- public child ``ProductSearchGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ProductSearchGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseProductSearchRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ProductSearchRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
