Column Families
===============

When creating a
:class:`ColumnFamily <google.cloud.bigtable.column_family.ColumnFamily>`, it is
possible to set garbage collection rules for expired data.

By setting a rule, cells in the table matching the rule will be deleted
during periodic garbage collection (which executes opportunistically in the
background).

The types
:class:`MaxAgeGCRule <google.cloud.bigtable.column_family.MaxAgeGCRule>`,
:class:`MaxVersionsGCRule <google.cloud.bigtable.column_family.MaxVersionsGCRule>`,
:class:`GarbageCollectionRuleUnion <google.cloud.bigtable.column_family.GarbageCollectionRuleUnion>` and
:class:`GarbageCollectionRuleIntersection <google.cloud.bigtable.column_family.GarbageCollectionRuleIntersection>`
can all be used as the optional ``gc_rule`` argument in the
:class:`ColumnFamily <google.cloud.bigtable.column_family.ColumnFamily>`
constructor. This value is then used in the
:meth:`create() <google.cloud.bigtable.column_family.ColumnFamily.create>` and
:meth:`update() <google.cloud.bigtable.column_family.ColumnFamily.update>` methods.

These rules can be nested arbitrarily, with a
:class:`MaxAgeGCRule <google.cloud.bigtable.column_family.MaxAgeGCRule>` or
:class:`MaxVersionsGCRule <google.cloud.bigtable.column_family.MaxVersionsGCRule>`
at the lowest level of the nesting:

.. code:: python

    import datetime

    max_age = datetime.timedelta(days=3)
    rule1 = MaxAgeGCRule(max_age)
    rule2 = MaxVersionsGCRule(1)

    # Make a composite that matches anything older than 3 days **AND**
    # with more than 1 version.
    rule3 = GarbageCollectionIntersection(rules=[rule1, rule2])

    # Make another composite that matches our previous intersection
    # **OR** anything that has more than 3 versions.
    rule4 = GarbageCollectionRule(max_num_versions=3)
    rule5 = GarbageCollectionUnion(rules=[rule3, rule4])

----

.. automodule:: google.cloud.bigtable.column_family
  :members:
  :show-inheritance:
