
transport inheritance structure
_______________________________

``PredictionApiKeyRegistryTransport`` is the ABC for all transports.

- public child ``PredictionApiKeyRegistryGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PredictionApiKeyRegistryGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePredictionApiKeyRegistryRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PredictionApiKeyRegistryRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
