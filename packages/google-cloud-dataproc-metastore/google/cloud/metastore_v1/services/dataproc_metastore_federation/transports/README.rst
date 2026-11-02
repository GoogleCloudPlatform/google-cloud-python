
transport inheritance structure
_______________________________

``DataprocMetastoreFederationTransport`` is the ABC for all transports.

- public child ``DataprocMetastoreFederationGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataprocMetastoreFederationGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataprocMetastoreFederationRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataprocMetastoreFederationRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
