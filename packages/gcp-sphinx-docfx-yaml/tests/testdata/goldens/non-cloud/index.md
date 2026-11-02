
# Welcome to pandas-gbq’s documentation!

The `pandas_gbq` module provides a wrapper for Google’s BigQuery
analytics web service to simplify retrieving results from BigQuery tables
using SQL-like queries. Result sets are parsed into a [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame)
with a shape and data types derived from the source table. Additionally,
DataFrames can be inserted into new BigQuery tables or appended to existing
tables.

**NOTE**: To use this module, you will need a valid BigQuery account. Use the
[BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox) to
try the service for free.

While BigQuery uses standard SQL syntax, it has some important differences
from traditional databases both in functionality, API limitations (size and
quantity of queries or uploads), and how Google charges for use of the
service. BiqQuery is best for analyzing large sets of data quickly. It is not
a direct replacement for a transactional database. Refer to the [BigQuery
Documentation](https://cloud.google.com/bigquery/what-is-bigquery) for
details on the service itself.

Contents:


* [Installation](install.md)


    * [Conda](install.md#conda)


    * [Pip](install.md#pip)


    * [Install from Source](install.md#install-from-source)


    * [Dependencies](install.md#dependencies)


* [Introduction](intro.md)


    * [Authenticating to BigQuery](intro.md#authenticating-to-bigquery)


    * [Reading data from BigQuery](intro.md#reading-data-from-bigquery)


    * [Writing data to BigQuery](intro.md#writing-data-to-bigquery)


* [Authentication](howto/authentication.md)


    * [Default Authentication Methods](howto/authentication.md#default-authentication-methods)


    * [Authenticating with a Service Account](howto/authentication.md#authenticating-with-a-service-account)


    * [Authenticating with a User Account](howto/authentication.md#authenticating-with-a-user-account)


    * [Authenticating from Highly Constrained Development Environments](howto/authentication.md#authenticating-from-highly-constrained-development-environments)


* [Reading Tables](reading.md)


    * [Querying with legacy SQL syntax](reading.md#querying-with-legacy-sql-syntax)


    * [Inferring the DataFrame’s dtypes](reading.md#inferring-the-dataframe-s-dtypes)


    * [Improving download performance](reading.md#improving-download-performance)


    * [Advanced configuration](reading.md#advanced-configuration)


* [Writing Tables](writing.md)


    * [Writing to an Existing Table](writing.md#writing-to-an-existing-table)


    * [Inferring the Table Schema](writing.md#inferring-the-table-schema)


    * [Troubleshooting Errors](writing.md#troubleshooting-errors)


* [API Reference](api.md)


* [Contributing to pandas-gbq](contributing.md)


    * [Where to start?](contributing.md#where-to-start)


    * [Bug reports and enhancement requests](contributing.md#bug-reports-and-enhancement-requests)


    * [Working with the code](contributing.md#working-with-the-code)


    * [Contributing to the code base](contributing.md#contributing-to-the-code-base)


    * [Contributing your changes to *pandas-gbq*](contributing.md#contributing-your-changes-to-pandas-gbq)


* [Changelog](changelog.md)


    * [0.19.1 (2023-01-25)](changelog.md#id1)


    * [0.19.0 (2023-01-11)](changelog.md#id2)


    * [0.18.1 (2022-11-28)](changelog.md#id3)


    * [0.18.0 (2022-11-19)](changelog.md#id4)


    * [0.17.9 (2022-09-27)](changelog.md#id6)


    * [0.17.8 (2022-08-09)](changelog.md#id7)


    * [0.17.7 (2022-07-11)](changelog.md#id9)


    * [0.17.6 (2022-06-03)](changelog.md#id11)


    * [0.17.5 (2022-05-09)](changelog.md#id13)


    * [0.17.4 (2022-03-14)](changelog.md#id15)


    * [0.17.3 (2022-03-05)](changelog.md#id17)


    * [0.17.2 (2022-03-02)](changelog.md#id19)


    * [0.17.1 (2022-02-24)](changelog.md#id21)


    * [0.17.0 (2022-01-19)](changelog.md#id24)


    * [0.16.0 (2021-11-08)](changelog.md#id27)


    * [0.15.0 / 2021-03-30](changelog.md#id31)


    * [0.14.1 / 2020-11-10](changelog.md#id35)


    * [0.14.0 / 2020-10-05](changelog.md#id37)


    * [0.13.3 / 2020-09-30](changelog.md#id38)


    * [0.13.2 / 2020-05-14](changelog.md#id39)


    * [0.13.1 / 2020-02-13](changelog.md#id40)


    * [0.13.0 / 2019-12-12](changelog.md#id41)


    * [0.12.0 / 2019-11-25](changelog.md#id42)


    * [0.11.0 / 2019-07-29](changelog.md#id46)


    * [0.10.0 / 2019-04-05](changelog.md#id48)


    * [0.9.0 / 2019-01-11](changelog.md#id53)


    * [0.8.0 / 2018-11-12](changelog.md#id54)


    * [0.7.0 / 2018-10-19](changelog.md#id58)


    * [0.6.1 / 2018-09-11](changelog.md#id60)


    * [0.6.0 / 2018-08-15](changelog.md#id61)


    * [0.5.0 / 2018-06-15](changelog.md#id62)


    * [0.4.1 / 2018-04-05](changelog.md#id65)


    * [0.4.0 / 2018-04-03](changelog.md#id66)


    * [0.3.1 / 2018-02-13](changelog.md#id67)


    * [0.3.0 / 2018-01-03](changelog.md#id68)


    * [0.2.1 / 2017-11-27](changelog.md#id69)


    * [0.2.0 / 2017-07-24](changelog.md#id70)


    * [0.1.6 / 2017-05-03](changelog.md#id71)


    * [0.1.4 / 2017-03-17](changelog.md#id72)


    * [0.1.3 / 2017-03-04](changelog.md#id73)


    * [0.1.2 / 2017-02-23](changelog.md#id74)


* [Privacy](privacy.md)


    * [Google account and user data](privacy.md#google-account-and-user-data)


    * [Policies for application authors](privacy.md#policies-for-application-authors)


* [Sign in to BigQuery](oauth.md)


# Indices and tables


* [Index](genindex.md)


* [Module Index](py-modindex.md)


* [Search Page](search.md)

<!-- Use the meta tags to verify the site for use in Google OAuth2 consent flow. -->
