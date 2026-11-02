# Custom Metric Exporter
The custom metric exporter, as defined in [metrics_exporter.py](./metrics_exporter.py), is designed to work in conjunction with OpenTelemetry and the Spanner client. It converts data into its protobuf equivalent and sends it to Google Cloud Monitoring.

## Filtering Criteria
The exporter filters metrics based on the following conditions, utilizing values defined in [constants.py](./constants.py):

* Metrics with a scope set to `gax-python`.
* Metrics with one of the following predefined names:
  * `attempt_latencies`
  * `attempt_count`
  * `operation_latencies`
  * `operation_count`
  * `gfe_latencies`
  * `gfe_connectivity_error_count`
  * `afe_latencies`
  * `afe_connectivity_error_count`

## Service Endpoint
The exporter sends metrics to the Google Cloud Monitoring [service endpoint](https://cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_create_service_time_series), distinct from the regular client endpoint. This service endpoint operates under a different quota limit than the user endpoint and features an additional server-side filter that only permits a predefined set of metrics to pass through.

When introducing new service metrics, it is essential to ensure they are allowed through by the server-side filter as well.
