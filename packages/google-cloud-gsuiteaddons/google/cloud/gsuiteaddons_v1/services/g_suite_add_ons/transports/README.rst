
transport inheritance structure
_______________________________

``GSuiteAddOnsTransport`` is the ABC for all transports.

- public child ``GSuiteAddOnsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GSuiteAddOnsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGSuiteAddOnsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GSuiteAddOnsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
