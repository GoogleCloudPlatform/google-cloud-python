
transport inheritance structure
_______________________________

``GlobalVmExtensionPoliciesTransport`` is the ABC for all transports.

- public child ``GlobalVmExtensionPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GlobalVmExtensionPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGlobalVmExtensionPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GlobalVmExtensionPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
