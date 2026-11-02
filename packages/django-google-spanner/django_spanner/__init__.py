# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import datetime
import os

# Monkey-patch AutoField to generate a random value since Cloud Spanner can't
# do that.
from uuid import uuid4

import django
from django.db import DEFAULT_DB_ALIAS
from django.db.models import JSONField
from django.db.models.fields import (
    NOT_PROVIDED,
    AutoField,
    BigAutoField,
    Field,
    SmallAutoField,
)

# Monkey-patch google.DatetimeWithNanoseconds's __eq__ compare against
# datetime.datetime.
from google.api_core.datetime_helpers import (
    DatetimeWithNanoseconds,
)
from google.cloud.spanner_v1 import JsonObject

from .functions import register_functions
from .lookups import register_lookups
from .utils import check_django_compatability
from .version import __version__

RANDOM_ID_GENERATION_ENABLED_SETTING = "RANDOM_ID_GENERATION_ENABLED"

USE_EMULATOR = os.getenv("SPANNER_EMULATOR_HOST") is not None

SUPPORTED_DJANGO_VERSIONS = [(6, 0), (5, 2)]

check_django_compatability(SUPPORTED_DJANGO_VERSIONS)

__all__ = ["__version__", "USE_EMULATOR"]
register_functions()
register_lookups()


def gen_rand_int64():
    # Credit to https://stackoverflow.com/a/3530326.
    return uuid4().int & 0x7FFFFFFFFFFFFFFF


def autofield_init(self, *args, **kwargs):
    kwargs["blank"] = True
    Field.__init__(self, *args, **kwargs)

    # The following behavior is chosen to prevent breaking changes with the original behavior.
    # 1. We use a client-side randomly generated int64 value for autofields if Spanner is the
    #    default database, and DISABLE_RANDOM_ID_GENERATION has not been set.
    # 2. If Spanner is one of the non-default databases, and no value at all has been set for
    #    DISABLE_RANDOM_ID_GENERATION, then we do not enable it. If there is a value for this
    #    configuration option, then we use that value.
    databases = django.db.connections.databases
    for db, config in databases.items():
        default_enabled = str(db == DEFAULT_DB_ALIAS)
        if (
            config["ENGINE"] == "django_spanner"
            and self.default == NOT_PROVIDED
            and config.get(
                RANDOM_ID_GENERATION_ENABLED_SETTING, default_enabled
            ).lower()
            == "true"
        ):
            self.default = gen_rand_int64
            self.db_returning = True
            self.validators = []
            break


AutoField.__init__ = autofield_init

SmallAutoField.__init__ = autofield_init
BigAutoField.__init__ = autofield_init


def get_prep_value(self, value):
    # Json encoding and decoding for spanner is done in python-spanner.
    if not isinstance(value, JsonObject) and isinstance(value, dict):
        return JsonObject(value)

    return value


JSONField.get_prep_value = get_prep_value

old_datetimewithnanoseconds_eq = getattr(DatetimeWithNanoseconds, "__eq__", None)


def datetimewithnanoseconds_eq(self, other):
    if old_datetimewithnanoseconds_eq:
        equal = old_datetimewithnanoseconds_eq(self, other)
        if equal:
            return True
        elif type(self) is type(other):
            return False

    # Otherwise try to convert them to an equvialent form.
    # See https://github.com/googleapis/python-spanner-django/issues/272
    if isinstance(other, datetime.datetime):
        return self.ctime() == other.ctime()

    return False


DatetimeWithNanoseconds.__eq__ = datetimewithnanoseconds_eq

# Sanity check here since tests can't easily be run for this file:
if __name__ == "__main__":
    from django.utils import timezone

    UTC = timezone.utc

    dt = datetime.datetime(2020, 1, 10, 2, 44, 57, 999, UTC)
    dtns = DatetimeWithNanoseconds(2020, 1, 10, 2, 44, 57, 999, UTC)
    equal = dtns == dt
    if not equal:
        raise Exception("%s\n!=\n%s" % (dtns, dt))
