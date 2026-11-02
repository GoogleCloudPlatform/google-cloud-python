
transport inheritance structure
_______________________________

``IAMConnectorCredentialsServiceTransport`` is the ABC for all transports.

- public child ``IAMConnectorCredentialsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``IAMConnectorCredentialsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseIAMConnectorCredentialsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``IAMConnectorCredentialsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
