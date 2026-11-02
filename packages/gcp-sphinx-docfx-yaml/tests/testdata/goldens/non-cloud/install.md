# Installation

You can install pandas-gbq with `conda`, `pip`, or by installing from source.

## Conda

```shell
$ conda install pandas-gbq --channel conda-forge
```

This installs pandas-gbq and all common dependencies, including `pandas`.

## Pip

To install the latest version of pandas-gbq: from the

```shell
$ pip install pandas-gbq -U
```

This installs pandas-gbq and all common dependencies, including `pandas`.

## Install from Source

```shell
$ pip install git+https://github.com/googleapis/python-bigquery-pandas.git
```

## Dependencies

This module requires following additional dependencies:


* [pydata-google-auth](https://github.com/pydata/pydata-google-auth): Helpers for authentication to Google’s API


* [pyarrow](https://arrow.apache.org/docs/python/): Format for getting data to/from Google BigQuery


* [google-auth](https://github.com/GoogleCloudPlatform/google-auth-library-python): authentication and authorization for Google’s API


* [google-auth-oauthlib](https://github.com/GoogleCloudPlatform/google-auth-library-python-oauthlib): integration with [oauthlib](https://github.com/idan/oauthlib) for end-user authentication


* [google-cloud-bigquery](https://googleapis.dev/python/bigquery/latest/index.html): Google Cloud client library for BigQuery


* [google-cloud-bigquery-storage](https://googleapis.dev/python/bigquerystorage/latest/index.html): Google Cloud client library for BigQuery Storage API

**NOTE**: The dependency on [google-cloud-bigquery](https://googleapis.dev/python/bigquery/latest/index.html) is new in version 0.3.0 of `pandas-gbq`.
Versions less than 0.3.0 required the following dependencies:


* [httplib2](https://github.com/httplib2/httplib2): HTTP client (no longer required)


* [google-api-python-client](http://github.com/google/google-api-python-client): Google’s API client (no longer required, replaced by [google-cloud-bigquery](hhttps://googleapis.dev/python/bigquery/latest/index.html):)


* [google-auth](https://github.com/GoogleCloudPlatform/google-auth-library-python): authentication and authorization for Google’s API


* [google-auth-oauthlib](https://github.com/GoogleCloudPlatform/google-auth-library-python-oauthlib): integration with [oauthlib](https://github.com/idan/oauthlib) for end-user authentication


* [google-auth-httplib2](https://github.com/GoogleCloudPlatform/google-auth-library-python-httplib2): adapter to use `httplib2` HTTP client with `google-auth` (no longer required)
