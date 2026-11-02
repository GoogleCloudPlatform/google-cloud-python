
transport inheritance structure
_______________________________

``CompanyServiceTransport`` is the ABC for all transports.

- public child ``CompanyServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CompanyServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCompanyServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CompanyServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
