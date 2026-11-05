
transport inheritance structure
_______________________________

``FolderGlobalVmExtensionPoliciesTransport`` is the ABC for all transports.

- public child ``FolderGlobalVmExtensionPoliciesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FolderGlobalVmExtensionPoliciesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFolderGlobalVmExtensionPoliciesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FolderGlobalVmExtensionPoliciesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
