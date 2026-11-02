
transport inheritance structure
_______________________________

``CloudSchedulerTransport`` is the ABC for all transports.

- public child ``CloudSchedulerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudSchedulerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudSchedulerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudSchedulerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
