
transport inheritance structure
_______________________________

``SaasRolloutsTransport`` is the ABC for all transports.

- public child ``SaasRolloutsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SaasRolloutsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSaasRolloutsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SaasRolloutsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
