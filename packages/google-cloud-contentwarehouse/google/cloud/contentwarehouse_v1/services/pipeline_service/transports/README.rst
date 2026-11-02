
transport inheritance structure
_______________________________

``PipelineServiceTransport`` is the ABC for all transports.

- public child ``PipelineServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PipelineServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePipelineServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PipelineServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
