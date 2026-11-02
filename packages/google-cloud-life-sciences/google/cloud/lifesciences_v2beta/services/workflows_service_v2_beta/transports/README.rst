
transport inheritance structure
_______________________________

``WorkflowsServiceV2BetaTransport`` is the ABC for all transports.

- public child ``WorkflowsServiceV2BetaGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``WorkflowsServiceV2BetaGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseWorkflowsServiceV2BetaRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``WorkflowsServiceV2BetaRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
