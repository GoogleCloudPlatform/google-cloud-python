# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import django
import sqlparse
from django.core.exceptions import ImproperlyConfigured


def check_django_compatability(supported_django_versions):
    """
    Verify that this version of django-spanner is compatible with the installed
    version of Django. For example, django-spanner is compatible
    with Django 5.2.x and 6.0.y
    """
    from . import __version__

    if django.VERSION[:2] not in supported_django_versions:
        raise ImproperlyConfigured(
            "You must use the latest version of django-spanner {A}.{B}.x "
            "with Django {A}.{B}.y (found django-spanner {C}).".format(
                A=django.VERSION[0], B=django.VERSION[1], C=__version__
            )
        )


def add_dummy_where(sql):
    """
    Cloud Spanner requires a WHERE clause on UPDATE and DELETE statements.
    Add a dummy WHERE clause if necessary.

    :type sql: str
    :param sql: A SQL statement.

    :rtype: str
    :returns: A SQL statement with dummy WHERE clause.
    """
    if any(isinstance(token, sqlparse.sql.Where) for token in sqlparse.parse(sql)[0]):
        return sql
    return sql + " WHERE 1=1"
