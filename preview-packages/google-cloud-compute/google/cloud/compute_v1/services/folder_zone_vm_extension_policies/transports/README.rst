
transport inheritance structure
_______________________________

``FolderZoneVmExtensionPoliciesTransport`` is the ABC for all transports.

- public child ``FolderZoneVmExtensionPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FolderZoneVmExtensionPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFolderZoneVmExtensionPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FolderZoneVmExtensionPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
