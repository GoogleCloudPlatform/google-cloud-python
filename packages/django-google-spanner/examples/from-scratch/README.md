## django-spanner for Django tutorial

This example shows how to use django-spanner for Cloud Spanner as a backend database for [Django's tutorials](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)

*NOTE:* Use the version of python-spanner-django that corresponds to your version of Django. For example, python-spanner-django 2.2.x works with Django 2.2.y. (This is the only supported version at this time.)

### Table of contents
- [Install django-spanner](#install-django-spanner)
- [Ensure you have a Cloud Spanner database already created](#ensure-you-have-a-cloud-spanner-database-already-created)
- [Follow the tutorial](#follow-the-tutorial)
- [Update your settings.py file to use django-spanner](#update-your-settings.py-file-to-use-django-spanner)
- [Set credentials and project environment variables](#Set-credentials-and-project-environment-variables)
- [Apply the migrations](#apply-the-migrations)
- [Now run your server](#now-run-your-server)
- [Create an Django admin user](#create-an-django-admin-user)
- [Login as admin](#login-as-admin)
- [Create and register your first model](#create-and-register-your-first-model)
- [References](#references)

### Install django-spanner
To install from PyPI:
```shell
pip3 install django-google-spanner
```
To install from source:
```shell
git clone https://github.com/googleapis/python-spanner-django
cd python-spanner-django/
pip3 install .
```

### Ensure you have a Cloud Spanner database already created
If you haven't already, please follow the steps to install [Cloud Spanner](https://cloud.google.com/spanner/docs/getting-started/set-up),
or visit this [codelab](https://opencensus.io/codelabs/spanner/#0)

**You'll need to ensure that your Google Application Default Credentials are properly downloaded and saved in your environment.**

### Follow the tutorial
Please follow the guides in https://docs.djangoproject.com/en/2.2/intro/tutorial01/ until the end with a single DISTINCTION:

### Update your settings.py file to use django-spanner
After we have a Cloud Spanner database created, we'll need a few variables:
* ProjectID
* Instance name
* Database name aka DisplayName

Once in, edit the DATABASES section of your mysite/settings.py file to the following:

a) add `django_spanner` as the very first entry to your `INSTALLED_APPS`
```python
INSTALLED_APPS = [
    'django_spanner',  # Must be listed first.
    ...
]
```

b) update `DATABASES` into the following:
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
* `NAME`: db1

which when filled out, will look like this

```python
DATABASES = {
    'default': {
        'ENGINE': 'django_spanner',
        'PROJECT': 'spanner-appdev',
        'INSTANCE': 'instance',
        'NAME': 'db1',
    }
}
```

### Set credentials and project environment variables
You'll need to download a service account JSON key file and point to it using an environment variable:
```shell
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/keyfile.json
export GOOGLE_CLOUD_PROJECT=gcloud_project
```

### Apply the migrations
Please run:
```shell
$ python3 manage.py migrate
```

and that'll take a while running, but when done, it will look like the following

<details>

```shell
$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
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
  Applying sessions.0001_initial... OK
```
</details>

After this you should can see the tables and indices created in your Cloud Spanner console

### Now run your server
After those migrations are completed, that will be all. Please continue on with the guides.

### Create an Django admin user
First you’ll need to create a user who can login to the admin site. Run the following command:

```shell
$ python3 manage.py createsuperuser
```
which will then produce a prompt which will allow you to create your super user
```shell
Username: admin
Email address: admin@example.com
Password: **********
Password (again): **********
Superuser created successfully.
```

### Login as admin
Let’s run the server
```shell script
python3 manage.py runserver
```
Then visit http://127.0.0.1:8000/admin/

### Create and register your first model
Please follow the guides in https://docs.djangoproject.com/en/2.2/intro/tutorial02/#creating-models
to create and register the model to the Django’s automatically-generated admin site.


### References

Resource|URL
---|---
Cloud Spanner homepage|https://cloud.google.com/spanner/
django-spanner project's source code|https://github.com/googleapis/python-spanner-django/
