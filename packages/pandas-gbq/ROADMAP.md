# pandas-gbq Roadmap

The purpose of this package is to provide a small subset of BigQuery
functionality that maps well to
[pandas.read_gbq](https://pandas.pydata.org/docs/reference/api/pandas.read_gbq.html#pandas.read_gbq)
and
[pandas.DataFrame.to_gbq](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_gbq.html#pandas.DataFrame.to_gbq).
Those methods in the pandas library are a thin wrapper to the equivalent
methods in this package.

## Adding features to pandas-gbq

Considerations when adding new features to pandas-gbq:

* New method? Consider an alternative, as the core focus of this library is
  `read_gbq` and `to_gbq`.
* Breaking change to an existing parameter? Consider an alternative, as folks
  could be using an older version of `pandas` that doesn't account for the
  change when a newer version of `pandas-gbq` is installed. If you must, please
  follow a 1+ year deprecation timeline.
* New parameter? Go for it! Be sure to also send a PR to `pandas` after the
  feature is released so that folks using the `pandas` wrapper can take
  advantage of it.
* New data type? OK. If there's not a good mapping to an existing `pandas`
  dtype, consider adding one to the `db-dtypes` package.

## Vision

The `pandas-gbq` package should do the "right thing" by default. This means you
should carefully choose dtypes for maximum compatibility with BigQuery and
avoid data loss. As new data types are added to BigQuery that don't have good
equivalents yet in the `pandas` ecosystem, equivalent dtypes should be added to
the `db-dtypes` package.

As new features are added that might improve performance, `pandas-gbq` should
offer easy ways to use them without sacrificing usability. For example, one
might consider using the `api_method` parameter of `to_gbq` to support the
BigQuery Storage Write API.

A note on `pandas.read_sql`: we'd like to be compatible with this too, for folks
that need better performance compared to the SQLAlchemy connector.

## Usability

Unlike the more object-oriented client-libraries, it's natural to have a method
with many parameters in the Python data science ecosystem. That said, the
`configuration` argument is provided, which takes the REST representation of
the job configuration so that power users can use new features without the need
for an explicit parameter being added.

## Conclusion

Keep it simple.

Don't break existing users.

Do the right thing by default.
