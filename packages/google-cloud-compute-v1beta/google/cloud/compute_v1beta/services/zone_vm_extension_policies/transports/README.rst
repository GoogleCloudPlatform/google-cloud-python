
transport inheritance structure
_______________________________

``ZoneVmExtensionPoliciesTransport`` is the ABC for all transports.

- public child ``ZoneVmExtensionPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ZoneVmExtensionPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseZoneVmExtensionPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ZoneVmExtensionPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
