
transport inheritance structure
_______________________________

``HostsTransport`` is the ABC for all transports.

- public child ``HostsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``HostsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseHostsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``HostsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
