
transport inheritance structure
_______________________________

``AccountIssueServiceTransport`` is the ABC for all transports.

- public child ``AccountIssueServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AccountIssueServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAccountIssueServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AccountIssueServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
