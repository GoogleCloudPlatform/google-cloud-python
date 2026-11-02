
transport inheritance structure
_______________________________

``WorkflowTemplateServiceTransport`` is the ABC for all transports.

- public child ``WorkflowTemplateServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``WorkflowTemplateServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseWorkflowTemplateServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``WorkflowTemplateServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
