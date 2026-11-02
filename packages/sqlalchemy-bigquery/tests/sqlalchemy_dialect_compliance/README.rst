==================================
SQLAlchemy Dialog Compliance Tests
==================================

SQLAlchemy provides reusable tests that test that SQLAlchemy dialects
work properly. This directory applies these tests to the BigQuery
SQLAlchemy dialect.

These are "system" tests, meaning that they run against a real
BigQuery account. To run the tests, you need a BigQuery account with
empty `test_schema` schema. Other test schemas will be created on the
fly. You need to have the `GOOGLE_APPLICATION_CREDENTIALS` environment
variable set to the path of a Google Cloud authentication file.
