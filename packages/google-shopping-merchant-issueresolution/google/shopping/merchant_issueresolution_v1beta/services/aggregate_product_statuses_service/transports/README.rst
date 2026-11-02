
transport inheritance structure
_______________________________

``AggregateProductStatusesServiceTransport`` is the ABC for all transports.

- public child ``AggregateProductStatusesServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AggregateProductStatusesServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAggregateProductStatusesServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AggregateProductStatusesServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
