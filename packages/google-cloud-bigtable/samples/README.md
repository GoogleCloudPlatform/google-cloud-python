# Python Code Samples for Cloud Bigtable

This directory contains code samples for Cloud Bigtable, which may be used as a reference for using this product.

## Prerequisites

1. If this is your first time working with GCP products, you will need to set up [the Cloud SDK][cloud_sdk] or utilize [Google Cloud Shell][gcloud_shell]. This sample may [require authentication][authentication] and you will need to [enable billing][enable_billing].

2. Set your environment variables:
   ```bash
   export GOOGLE_CLOUD_PROJECT="your-project-id"
   export BIGTABLE_INSTANCE="your-instance-id"
   ```

## Running Samples and Tests

1. Install dependencies for the sample module you want to run:
   ```bash
   pip install -r requirements.txt
   ```

2. Run sample scripts directly:
   ```bash
   python main.py $GOOGLE_CLOUD_PROJECT $BIGTABLE_INSTANCE
   ```

3. To run the sample tests using Nox, from the `packages/google-cloud-bigtable` directory:
   ```bash
   nox -s samples
   ```
   This installs the library from the repository checkout, so the samples are
   tested against the code at HEAD. To run a subset, pass a path:
   ```bash
   nox -s samples -- samples/legacy_client/quickstart
   ```

## Additional Information

You can read the documentation for more details on API usage and use GitHub
to <a href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-bigtable">browse the source</a> and [report issues][issues].

### Contributing

View the [contributing guidelines][contrib_guide] and the [Python style guide][py_style] for more information.

[authentication]: https://cloud.google.com/docs/authentication/getting-started
[enable_billing]: https://cloud.google.com/apis/docs/getting-started#enabling_billing
[client_library_python]: https://googlecloudplatform.github.io/google-cloud-python/
[issues]: https://github.com/googleapis/google-cloud-python/issues
[contrib_guide]: https://github.com/googleapis/google-cloud-python/blob/main/CONTRIBUTING.rst
[py_style]: http://google.github.io/styleguide/pyguide.html
[cloud_sdk]: https://cloud.google.com/sdk/docs
[gcloud_shell]: https://cloud.google.com/shell/docs
