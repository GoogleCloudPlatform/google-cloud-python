
transport inheritance structure
_______________________________

``TargetVpnGatewaysTransport`` is the ABC for all transports.

- public child ``TargetVpnGatewaysGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TargetVpnGatewaysGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTargetVpnGatewaysRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TargetVpnGatewaysRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
