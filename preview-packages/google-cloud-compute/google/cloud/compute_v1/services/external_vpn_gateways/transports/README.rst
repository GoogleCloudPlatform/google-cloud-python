
transport inheritance structure
_______________________________

``ExternalVpnGatewaysTransport`` is the ABC for all transports.

- public child ``ExternalVpnGatewaysGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ExternalVpnGatewaysGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseExternalVpnGatewaysRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ExternalVpnGatewaysRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
