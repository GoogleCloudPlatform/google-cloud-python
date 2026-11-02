
transport inheritance structure
_______________________________

``AutomaticImprovementsServiceTransport`` is the ABC for all transports.

- public child ``AutomaticImprovementsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AutomaticImprovementsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAutomaticImprovementsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AutomaticImprovementsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
