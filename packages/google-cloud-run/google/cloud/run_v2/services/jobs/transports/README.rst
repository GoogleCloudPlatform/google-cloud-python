
transport inheritance structure
_______________________________

``JobsTransport`` is the ABC for all transports.

- public child ``JobsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``JobsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseJobsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``JobsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
