#!/bin/sh

# Copyright (c) 2020 Google LLC. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

set -x pipefail

# Disable buffering, so that the logs stream through.
export PYTHONUNBUFFERED=1

export DJANGO_TESTS_DIR="django_tests_dir"
mkdir -p $DJANGO_TESTS_DIR

pip3 install .
# Clone Django 5.2 (assuming stable/5.2.x exists, update if needed)
if [ ! -d "$DJANGO_TESTS_DIR/django" ]; then
    git clone --depth 1 --single-branch --branch "stable/5.2.x" https://github.com/django/django.git $DJANGO_TESTS_DIR/django
fi

cd $DJANGO_TESTS_DIR/django && pip3 install -e . && pip3 install -r tests/requirements/py3.txt; cd ../../
pip3 install google-cloud-testutils

# Only add the current directory (project root) to PYTHONPATH so django_spanner is importable.
# Do NOT add django_tests_dir, as it causes 'django' to be imported as a namespace package.
export PYTHONPATH=$PYTHONPATH:$(pwd):$(pwd)/$DJANGO_TESTS_DIR/django

python3 create_test_instance.py

# If no SPANNER_TEST_DB is set, generate a unique one
# so that we can have multiple tests running without
# conflicting which changes and constraints. We'll always
# cleanup the created database.
TEST_DBNAME=${SPANNER_TEST_DB:-$(python3 -c 'import os, time; print(chr(ord("a") + time.time_ns() % 26)+os.urandom(10).hex())')}
TEST_DBNAME_OTHER="$TEST_DBNAME-ot"
INSTANCE=${SPANNER_TEST_INSTANCE:-spanner-django-python-systest}
PROJECT=${PROJECT_ID:-$GOOGLE_CLOUD_PROJECT}
SETTINGS_FILE="$TEST_DBNAME-settings"
TESTS_DIR=${DJANGO_TESTS_DIR:-django_tests}

create_settings() {
    cat << ! > "$SETTINGS_FILE.py"
import django_spanner
DATABASES = {
   'default': {
       'ENGINE': 'django_spanner',
       'PROJECT': "$PROJECT",
       'INSTANCE': "$INSTANCE",
       'NAME': "$TEST_DBNAME",
   },
   'other': {
       'ENGINE': 'django_spanner',
       'PROJECT': "$PROJECT",
       'INSTANCE': "$INSTANCE",
       'NAME': "$TEST_DBNAME_OTHER",
   },
}
USE_TZ = False
SECRET_KEY = 'spanner_tests_secret_key'
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tests.system.django_spanner',
]
!
}

cd $TESTS_DIR/django/tests
create_settings

EXIT_STATUS=0
for DJANGO_TEST_APP in $DJANGO_TEST_APPS
do
   if [ "$DJANGO_TEST_APP" = "order_with_respect_to" ] || [ "$DJANGO_TEST_APP" = "contenttypes_tests" ] || [ "$DJANGO_TEST_APP" = "inspectdb" ]; then
       echo "Skipping $DJANGO_TEST_APP as it is incompatible with Spanner"
       continue
   fi
   python3 runtests.py $DJANGO_TEST_APP --verbosity=3 --noinput --settings $SETTINGS_FILE || EXIT_STATUS=$?
done
exit $EXIT_STATUS
