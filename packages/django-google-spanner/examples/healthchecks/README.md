## django-spanner on healthchecks.io

This example shows how to use django-spanner for Cloud Spanner as a backend database for [https://healthchecks.io](https://healthchecks.io)

### Table of contents
- [Install healthchecks](#install-healthchecks)
- [Install django-spanner in the virtual-env](#install-django-spanner-in-the-virtual-env)
- [Ensure you have a Cloud Spanner database already created](#ensure-you-have-a-Cloud-Spanner-database-already-created)
- [Set credentials and project environment variables](#Set-credentials-and-project-environment-variables)
- [Update local_settings.py](#update-local_settings.py)
- [Run the server](#run-the-server)
- [Apply the migrations](#apply-the-migrations)
- [Go view the results on Cloud Spanner UI](#go-view-the-results-on-Cloud-Spanner-UI)
- [Run the application](#run-the-application)
- [References](#references)

### Install healthchecks
Please follow the instructions to install [healthchecks.io on Github](https://github.com/healthchecks/healthchecks/).
You'll need to active the virtual-env as their install instructions request.

### Install django-spanner in the virtual-env

Go to the directory in which you installed [healthchecks](#install-healthchecks)
and ensure your virtual-env is on. The prompt should look something like this:

```shell
(hc-venv) $
```

Install django-google-spanner from PyPI:

```shell
(h-venv) $ pip install django-google-spanner
```

### Ensure you have a Cloud Spanner database already created
If you haven't already, please follow the steps to install [Cloud Spanner](https://cloud.google.com/spanner/docs/getting-started/set-up),
or visit this [codelab](https://opencensus.io/codelabs/spanner/#0)

### Set credentials and project environment variables
You'll need to download a service account JSON keyfile and point to it using an environment variable:

```shell
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/keyfile.json
export GOOGLE_CLOUD_PROJECT=gcloud_project
```

### Update local_settings.py
After we have a Cloud Spanner database created, we'll need a few variables:
* ProjectID
* Instance name
* Database name aka DisplayName


*NOTE:* Healthchecks's  `local_settings.py` overrides the default settings
mentioned in `settings.py`.

There are two ways to edit settings file:
1. You can edit the file `hc/settings.py` to:

    a) Add `django_spanner` as the first entry to `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS = [
        'django_spanner',  # Must be listed first.
        ...
    ]
    ```

    b) Edit `DATABASES` into the following:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django_spanner',
            'PROJECT': PROJECT_ID,
            'INSTANCE': SPANNER_INSTANCE,
            'NAME': SPANNER_DATABASE_NAME,
        }
    }
    ```

2. You can edit the file `hc/local_settings.py` to:

    a) The `INSTALLED_APPS` MUST be copied from `hc/settings.py` to `hc/local_settings.py`
       and add `django_spanner` as the first entry to `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS = [
        'django_spanner',  # Must be listed first.
        ...
    ]
    ```

    b) Add or Edit `DATABASES` into the following:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django_spanner',
            'PROJECT': PROJECT_ID,
            'INSTANCE': SPANNER_INSTANCE,
            'NAME': SPANNER_DATABASE_NAME,
        }
    }
    ```

and for example here is a filled in database where:

* `PROJECT_ID`: spanner-appdev
* `INSTANCE`: instance
* `NAME`: healthchecks_db

which when filled out, will look like this

```python
DATABASES = {
    'default': {
        'ENGINE': 'django_spanner',
        'PROJECT': 'spanner-appdev',
        'INSTANCE': 'instance',
        'NAME': 'healthchecks_db',
    }
}
```

### Run the server
With those steps out of the way, and having successfully setup both healthchecks and properly installed django-spanner, we are now ready to get started

```shell
(hc-venv) $ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 120 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): accounts, admin, api, auth, contenttypes, payments, sessions.
Run 'python manage.py migrate' to apply them.

April 06, 2020 - 01:45:23
Django version 3.0.3, using settings 'hc.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C
```

### Apply the migrations
Please run:
```shell
(hc-venv) $ python3 manage.py migrate
Operations to perform:
  Apply all migrations: accounts, admin, api, auth, contenttypes, payments, sessions
Running migrations:
```

and that'll take a while running, but when done, it will look like the following

<details>

```shell
(hc-venv) $ python3 manage.py migrate
Operations to perform:
  Apply all migrations: accounts, admin, api, auth, contenttypes, payments, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying accounts.0001_initial... OK
  Applying accounts.0002_profile_ping_log_limit... OK
  Applying accounts.0003_profile_token... OK
  Applying accounts.0004_profile_api_key... OK
  Applying accounts.0005_auto_20160509_0801... OK
  Applying accounts.0006_profile_current_team... OK
  Applying accounts.0007_profile_check_limit... OK
  Applying accounts.0008_profile_bill_to... OK
  Applying accounts.0009_auto_20170714_1734... OK
  Applying accounts.0010_profile_team_limit... OK
  Applying accounts.0011_profile_sort... OK
  Applying accounts.0012_auto_20171014_1002... OK
  Applying accounts.0013_remove_profile_team_access_allowed... OK
  Applying accounts.0014_auto_20171227_1530... OK
  Applying accounts.0015_auto_20181029_1858... OK
  Applying accounts.0016_remove_profile_bill_to... OK
  Applying accounts.0017_auto_20190112_1426... OK
  Applying accounts.0018_auto_20190112_1426... OK
  Applying accounts.0019_project_badge_key... OK
  Applying accounts.0020_auto_20190112_1950... OK
  Applying accounts.0021_auto_20190112_2005... OK
  Applying accounts.0022_auto_20190114_0857... OK
  Applying accounts.0023_auto_20190117_1419... OK
  Applying accounts.0024_auto_20190119_1540... OK
  Applying accounts.0025_remove_member_team... OK
  Applying accounts.0026_auto_20190204_2042... OK
  Applying accounts.0027_profile_deletion_notice_date... OK
  Applying accounts.0028_auto_20191119_1346... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying api.0001_initial... OK
  Applying api.0002_auto_20150616_0732... OK
  Applying api.0003_auto_20150616_1249... OK
  Applying api.0004_auto_20150616_1319... OK
  Applying api.0005_auto_20150630_2021... OK
  Applying api.0006_check_grace... OK
  Applying api.0007_ping... OK
  Applying api.0008_auto_20150801_1213... OK
  Applying api.0009_auto_20150801_1250... OK
  Applying api.0010_channel... OK
  Applying api.0011_notification... OK
  Applying api.0012_auto_20150930_1922... OK
  Applying api.0013_auto_20151001_2029... OK
  Applying api.0014_auto_20151019_2039... OK
  Applying api.0015_auto_20151022_1008... OK
  Applying api.0016_auto_20151030_1107... OK
  Applying api.0017_auto_20151117_1032... OK
  Applying api.0018_remove_ping_body... OK
  Applying api.0019_check_tags... OK
  Applying api.0020_check_n_pings... OK
  Applying api.0021_ping_n... OK
  Applying api.0022_auto_20160130_2042... OK
  Applying api.0023_auto_20160131_1919... OK
  Applying api.0024_auto_20160203_2227... OK
  Applying api.0025_auto_20160216_1214... OK
  Applying api.0026_auto_20160415_1824... OK
  Applying api.0027_auto_20161213_1059... OK
  Applying api.0028_auto_20170305_1907... OK
  Applying api.0029_auto_20170507_1251... OK
  Applying api.0030_check_last_ping_body... OK
  Applying api.0031_auto_20170509_1320... OK
  Applying api.0032_auto_20170608_1158... OK
  Applying api.0033_auto_20170714_1715... OK
  Applying api.0034_auto_20171227_1530... OK
  Applying api.0035_auto_20171229_2008... OK
  Applying api.0036_auto_20180116_2243... OK
  Applying api.0037_auto_20180127_1215... OK
  Applying api.0038_auto_20180318_1306... OK
  Applying api.0039_remove_check_last_ping_body... OK
  Applying api.0040_auto_20180517_1336... OK
  Applying api.0041_check_desc... OK
  Applying api.0042_auto_20181029_1522... OK
  Applying api.0043_channel_name... OK
  Applying api.0044_auto_20181120_2004... OK
  Applying api.0045_flip... OK
  Applying api.0046_auto_20181218_1245... OK
  Applying api.0047_auto_20181225_2315... OK
  Applying api.0048_auto_20190102_0737... OK
  Applying api.0049_auto_20190102_0743... OK
  Applying api.0050_ping_kind... OK
  Applying api.0051_auto_20190104_0908... OK
  Applying api.0052_auto_20190104_1122... OK
  Applying api.0053_check_subject... OK
  Applying api.0054_auto_20190112_1427... OK
  Applying api.0055_auto_20190112_1427... OK
  Applying api.0056_auto_20190114_0857... OK
  Applying api.0057_auto_20190118_1319... OK
  Applying api.0058_auto_20190312_1716... OK
  Applying api.0059_auto_20190314_1744... OK
  Applying api.0060_tokenbucket... OK
  Applying api.0061_webhook_values... OK
  Applying api.0062_auto_20190720_1350... OK
  Applying api.0063_auto_20190903_0901... OK
  Applying api.0064_auto_20191119_1346... OK
  Applying api.0065_auto_20191127_1240... OK
  Applying api.0066_channel_last_error... OK
  Applying api.0067_last_error_values... OK
  Applying api.0068_auto_20200117_1023... OK
  Applying api.0069_auto_20200117_1227... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying payments.0001_initial... OK
  Applying payments.0002_subscription_plan_id... OK
  Applying payments.0003_subscription_address_id... OK
  Applying payments.0004_subscription_send_invoices... OK
  Applying payments.0005_subscription_plan_name... OK
  Applying payments.0006_subscription_invoice_email... OK
  Applying sessions.0001_initial... OK
```
</details>

### Go view the results on Cloud Spanner UI

To double check that the respective tables and migrations were performed, please go visit the page with your database on Cloud Spanner's UI.
For example it should look like this
![](/assets/healthchecks-db-overview.png)

### Run the application
And now you should be able to run the application and then visit the link to it by

```shell
(hc-venv) $ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 06, 2020 - 20:49:25
Django version 2.2.1, using settings 'hc.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[06/Apr/2020 20:49:35] "GET / HTTP/1.1" 200 29334
[06/Apr/2020 20:49:35] "GET /static/img/logo-full%402x.png HTTP/1.1" 200 8395
[06/Apr/2020 20:49:35] "GET /static/img/cron%402x.png HTTP/1.1" 200 31324
[06/Apr/2020 20:49:35] "GET /static/img/my_checks%402x.png HTTP/1.1" 200 29642
[06/Apr/2020 20:49:35] "GET /static/img/period_grace%402x.png HTTP/1.1" 200 23388
[06/Apr/2020 20:49:35] "GET /static/img/badges%402x.png HTTP/1.1" 200 28904
[06/Apr/2020 20:49:35] "GET /static/img/check_details%402x.png HTTP/1.1" 200 50342
[06/Apr/2020 20:49:35] "GET /static/img/favicon.ico HTTP/1.1" 200 5430
[06/Apr/2020 20:49:47] "POST /accounts/signup/ HTTP/1.1" 200 81
[06/Apr/2020 20:50:02] "POST /accounts/signup/ HTTP/1.1" 200 73
```

### References

Resource|URL
---|---
Healthchecks app|https://healthchecks.io/
Healthchecks source code|https://github.com/healthchecks/healthchecks/
Cloud Spanner homepage|https://cloud.google.com/spanner/
django-spanner project's source code|https://github.com/googleapis/python-spanner-django/
