
transport inheritance structure
_______________________________

``DhcpOptionsConfigsTransport`` is the ABC for all transports.

- public child ``DhcpOptionsConfigsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DhcpOptionsConfigsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDhcpOptionsConfigsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DhcpOptionsConfigsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
