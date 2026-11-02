
transport inheritance structure
_______________________________

``ChangelogsTransport`` is the ABC for all transports.

- public child ``ChangelogsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ChangelogsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseChangelogsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ChangelogsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
