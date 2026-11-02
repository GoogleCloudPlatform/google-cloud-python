# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import os

DEBUG = True
USE_TZ = True

INSTALLED_APPS = [
    "django_spanner",  # Must be the first entry
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tests",
]

TIME_ZONE = "UTC"

INSTANCE_ID = os.environ.get(
    "GOOGLE_CLOUD_TESTS_SPANNER_INSTANCE", "spanner-django-python-systest"
)

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "emulator-test-project")

# _get_test_db_name method in creation.py addes prefix of 'test_' to db name.
DATABASE_NAME = os.getenv("DJANGO_SPANNER_DB", "django_test_db")

DATABASES = {
    "default": {
        "ENGINE": "django_spanner",
        "PROJECT": PROJECT_ID,
        "INSTANCE": INSTANCE_ID,
        "NAME": DATABASE_NAME,
        "TEST": {"NAME": DATABASE_NAME},
    },
    "secondary": {
        "ENGINE": "django_spanner",
        "PROJECT": PROJECT_ID,
        "INSTANCE": INSTANCE_ID,
        "NAME": DATABASE_NAME,
        "TEST": {"NAME": DATABASE_NAME},
    },
    "other": {
        "ENGINE": "django.db.backends.sqlite3",
    },
}

SECRET_KEY = "spanner env secret key"

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

SITE_ID = 1

CONN_MAX_AGE = 60

ENGINE = "django_spanner"
PROJECT = "emulator-local"
INSTANCE = "django-test-instance"
NAME = "django_test_db"
OPTIONS = {}
AUTOCOMMIT = True
