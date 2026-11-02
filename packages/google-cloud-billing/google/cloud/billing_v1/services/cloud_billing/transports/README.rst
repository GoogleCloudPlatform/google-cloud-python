
transport inheritance structure
_______________________________

``CloudBillingTransport`` is the ABC for all transports.

- public child ``CloudBillingGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudBillingGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudBillingRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudBillingRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
