
transport inheritance structure
_______________________________

``VpnTunnelsTransport`` is the ABC for all transports.

- public child ``VpnTunnelsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``VpnTunnelsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseVpnTunnelsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``VpnTunnelsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
