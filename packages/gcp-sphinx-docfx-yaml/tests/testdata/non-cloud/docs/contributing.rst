.. _contributing:

**************************
Contributing to pandas-gbq
**************************

.. contents:: Table of contents:
   :local:

Where to start?
===============

All contributions, bug reports, bug fixes, documentation improvements,
enhancements and ideas are welcome.

If you are simply looking to start working with the *pandas-gbq* codebase, navigate to the
`GitHub "issues" tab <https://github.com/googleapis/python-bigquery-pandas/issues>`_ and start looking through
interesting issues.

Or maybe through using *pandas-gbq* you have an idea of your own or are looking for something
in the documentation and thinking 'this can be improved'...you can do something about it!

Feel free to ask questions on the `mailing list
<https://groups.google.com/forum/?fromgroups#!forum/pydata>`_.

Bug reports and enhancement requests
====================================

Bug reports are an important part of making *pandas-gbq* more stable.  Having a complete bug report
will allow others to reproduce the bug and provide insight into fixing it.  Because many versions of
*pandas-gbq* are supported, knowing version information will also identify improvements made since
previous versions. Trying the bug-producing code out on the *master* branch is often a worthwhile exercise
to confirm the bug still exists.  It is also worth searching existing bug reports and pull requests
to see if the issue has already been reported and/or fixed.

Bug reports must:

#. Include a short, self-contained Python snippet reproducing the problem.
   You can format the code nicely by using `GitHub Flavored Markdown
   <http://github.github.com/github-flavored-markdown/>`__

   .. code-block:: python

      >>> from pandas_gbq import gbq
      >>> df = gbq.read_gbq(...)
      ...

#. Include the full version string of *pandas-gbq*.

   .. code-block:: python

      >>> import pandas_gbq
      >>> pandas_gbq.__version__
      ...

#. Explain why the current behavior is wrong/not desired and what you expect instead.

The issue will then show up to the *pandas-gbq* community and be open to comments/ideas from others.

Working with the code
=====================

Now that you have an issue you want to fix, enhancement to add, or documentation to improve,
you need to learn how to work with GitHub and the *pandas-gbq* code base.

Version control, Git, and GitHub
--------------------------------

To the new user, working with Git is one of the more daunting aspects of contributing to *pandas-gbq*.
It can very quickly become overwhelming, but sticking to the guidelines below will help keep the process
straightforward and mostly trouble free.  As always, if you are having difficulties please
feel free to ask for help.

The code is hosted on `GitHub <https://www.github.com/googleapis/python-bigquery-pandas>`_. To
contribute you will need to sign up for a `free GitHub account
<https://github.com/signup/free>`_. We use `Git <http://git-scm.com/>`_ for
version control to allow many people to work together on the project.

Some great resources for learning Git:

* the `GitHub help pages <http://help.github.com/>`_.
* the `NumPy's documentation <http://docs.scipy.org/doc/numpy/dev/index.html>`_.
* Matthew Brett's `Pydagogue <http://matthew-brett.github.com/pydagogue/>`_.

Getting started with Git
------------------------

`GitHub has instructions <http://help.github.com/set-up-git-redirect>`__ for installing git,
setting up your SSH key, and configuring git.  All these steps need to be completed before
you can work seamlessly between your local repository and GitHub.

.. _contributing.forking:

Forking
-------

You will need your own fork to work on the code. Go to the `pandas-gbq project
page <https://github.com/googleapis/python-bigquery-pandas>`_ and hit the ``Fork`` button. You will
want to clone your fork to your machine::

    git clone git@github.com:your-user-name/pandas-gbq.git pandas-gbq-yourname
    cd pandas-gbq-yourname
    git remote add upstream git://github.com/googleapis/python-bigquery-pandas.git

This creates the directory `pandas-gbq-yourname` and connects your repository to
the upstream (main project) *pandas-gbq* repository.

The testing suite will run automatically on CircleCI once your pull request is submitted.
However, if you wish to run the test suite on a branch prior to submitting the pull request,
then CircleCI needs to be hooked up to your GitHub repository.  Instructions for doing so
are `here <https://circleci.com/docs/2.0/getting-started/>`__.

Creating a branch
-----------------

You want your master branch to reflect only production-ready code, so create a
feature branch for making your changes. For example::

    git branch shiny-new-feature
    git checkout shiny-new-feature

The above can be simplified to::

    git checkout -b shiny-new-feature

This changes your working directory to the shiny-new-feature branch.  Keep any
changes in this branch specific to one bug or feature so it is clear
what the branch brings to *pandas-gbq*. You can have many shiny-new-features
and switch in between them using the git checkout command.

To update this branch, you need to retrieve the changes from the master branch::

    git fetch upstream
    git rebase upstream/master

This will replay your commits on top of the latest pandas-gbq git master.  If this
leads to merge conflicts, you must resolve these before submitting your pull
request.  If you have uncommitted changes, you will need to ``stash`` them prior
to updating.  This will effectively store your changes and they can be reapplied
after updating.

Install in Development Mode
---------------------------

It's helpful to install pandas-gbq in development mode so that you can
use the library without reinstalling the package after every change.

Conda
~~~~~

Create a new conda environment and install the necessary dependencies

.. code-block:: shell

   $ conda create -n my-env --channel conda-forge  \
         db-dtypes \
         pandas \
         pydata-google-auth \
         google-cloud-bigquery
   $ source activate my-env

Install pandas-gbq in development mode

.. code-block:: shell

    $ python setup.py develop

Pip & virtualenv
~~~~~~~~~~~~~~~~

*Skip this section if you already followed the conda instructions.*

Create a new `virtual
environment <https://virtualenv.pypa.io/en/stable/userguide/>`__.

.. code-block:: shell

    $ virtualenv env
    $ source env/bin/activate

You can install pandas-gbq and its dependencies in `development mode via
pip <https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs>`__.

.. code-block:: shell

    $ pip install -e .

Contributing to the code base
=============================

.. contents:: Code Base:
   :local:

Code standards
--------------

Writing good code is not just about what you write. It is also about *how* you
write it. During testing on Travis-CI, several tools will be run to check your
code for stylistic errors. Generating any warnings will cause the test to fail.
Thus, good style is a requirement for submitting code to *pandas-gbq*.

In addition, because a lot of people use our library, it is important that we
do not make sudden changes to the code that could have the potential to break
a lot of user code as a result, that is, we need it to be as *backwards compatible*
as possible to avoid mass breakages.

Python (PEP8)
~~~~~~~~~~~~~

*pandas-gbq* uses the `PEP8 <http://www.python.org/dev/peps/pep-0008/>`_ standard.
There are several tools to ensure you abide by this standard. Here are *some* of
the more common ``PEP8`` issues:

  - we restrict line-length to 79 characters to promote readability
  - passing arguments should have spaces after commas, e.g. ``foo(arg1, arg2, kw1='bar')``

CircleCI will run the `'black' code formatting tool
<https://black.readthedocs.io/>`_ and report any stylistic errors in your
code. Therefore, it is helpful before submitting code to run the formatter
yourself::

    pip install black
    black .

Backwards Compatibility
~~~~~~~~~~~~~~~~~~~~~~~

Please try to maintain backward compatibility. If you think breakage is required,
clearly state why as part of the pull request.  Also, be careful when changing method
signatures and add deprecation warnings where needed.

Test-driven development/code writing
------------------------------------

*pandas-gbq* is serious about testing and strongly encourages contributors to embrace
`test-driven development (TDD) <http://en.wikipedia.org/wiki/Test-driven_development>`_.
This development process "relies on the repetition of a very short development cycle:
first the developer writes an (initially failing) automated test case that defines a desired
improvement or new function, then produces the minimum amount of code to pass that test."
So, before actually writing any code, you should write your tests.  Often the test can be
taken from the original GitHub issue.  However, it is always worth considering additional
use cases and writing corresponding tests.

Adding tests is one of the most common requests after code is pushed to *pandas-gbq*.  Therefore,
it is worth getting in the habit of writing tests ahead of time so this is never an issue.

Like many packages, *pandas-gbq* uses `pytest <http://doc.pytest.org/en/latest/>`_.

Running the test suite
~~~~~~~~~~~~~~~~~~~~~~

The tests can then be run directly inside your Git clone (without having to
install *pandas-gbq*) by typing::

    pytest tests/unit
    pytest tests/system.py

The tests suite is exhaustive and takes around 20 minutes to run.  Often it is
worth running only a subset of tests first around your changes before running the
entire suite.

The easiest way to do this is with::

    pytest tests/path/to/test.py -k regex_matching_test_name

Or with one of the following constructs::

    pytest tests/[test-module].py
    pytest tests/[test-module].py::[TestClass]
    pytest tests/[test-module].py::[TestClass]::[test_method]

For more, see the `pytest <http://doc.pytest.org/en/latest/>`_ documentation.

Testing on multiple Python versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pandas-gbq uses `nox <https://nox.readthedocs.io>`__ to automate testing in
multiple Python environments. First, install nox.

.. code-block:: shell

    $ pip install --upgrade nox-automation

To run tests in all versions of Python, run `nox` from the repository's root
directory.

.. _contributing.gbq_integration_tests:

Running Google BigQuery Integration Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need to create a Google BigQuery private key in JSON format in order
to run Google BigQuery integration tests on your local machine and on
CircleCI. The first step is to create a `service account
<https://console.cloud.google.com/iam-admin/serviceaccounts/>`__. Grant the
service account permissions to run BigQuery queries and to create datasets
and tables.

To run the integration tests locally, set the following environment variables
before running ``pytest``:

#. ``GBQ_PROJECT_ID`` with the value being the ID of your BigQuery project.
#. ``GBQ_GOOGLE_APPLICATION_CREDENTIALS`` with the value being the *path* to
   the JSON key that you downloaded for your service account.

Integration tests are skipped in pull requests because the credentials that
are required for running Google BigQuery integration tests are
`configured in the CircleCI web interface
<https://circleci.com/docs/2.0/env-vars/#setting-an-environment-variable-in-a-project>`_
and are only accessible from the googleapis/python-bigquery-pandas repository. The
credentials won't be available on forks of pandas-gbq. Here are the steps to
run gbq integration tests on a forked repository:

#. Go to `CircleCI <https://circleci.com/dashboard>`__ and sign in with your
   GitHub account.
#. Switch to your personal account in the top-left organization switcher.
#. Use the "Add projects" tab to enable CircleCI for your fork.
#. Click on the gear icon to edit your CircleCI build, and add two environment
   variables:

   - ``GBQ_PROJECT_ID`` with the value being the ID of your BigQuery project.

   - ``SERVICE_ACCOUNT_KEY`` with the value being the base64-encoded
     *contents* of the JSON key that you downloaded for your service account.

   Keep the contents of these variables confidential. These variables contain
   sensitive data and you do not want their contents being exposed in build
   logs.
#. Your branch should be tested automatically once it is pushed. You can check
   the status by visiting your Circle CI branches page which exists at the
   following location: https://circleci.com/gh/your-username/python-bigquery-pandas.
   Click on a build job for your branch.

Documenting your code
---------------------

Changes should follow convential commits.  The release-please bot uses the
commit message to create an ongoing change log.

If your code is an enhancement, it is most likely necessary to add usage
examples to the existing documentation. Further, to let users know when
this feature was added, the ``versionadded`` directive is used. The sphinx
syntax for that is:

.. code-block:: rst

  .. versionadded:: 0.1.3

This will put the text *New in version 0.1.3* wherever you put the sphinx
directive. This should also be put in the docstring when adding a new function
or method.

Contributing your changes to *pandas-gbq*
=========================================

Committing your code
--------------------

Keep style fixes to a separate commit to make your pull request more readable.

Once you've made changes, you can see them by typing::

    git status

If you have created a new file, it is not being tracked by git. Add it by typing::

    git add path/to/file-to-be-added.py

Doing 'git status' again should give something like::

    # On branch shiny-new-feature
    #
    #       modified:   /relative/path/to/file-you-added.py
    #

Finally, commit your changes to your local repository with an explanatory message.  *pandas-gbq*
uses `conventional commit message prefixes
<https://www.conventionalcommits.org/en/v1.0.0/>`_ and layout.  Here are some
common prefixes along with general guidelines for when to use them:

    * feat: Enhancement, new functionality
    * fix: Bug fix, performance improvement
    * doc: Additions/updates to documentation
    * deps: Change to package dependencies
    * test: Additions/updates to tests
    * chore: Updates to the build process/scripts
    * refactor: Code cleanup

The following defines how a commit message should be structured.  Please reference the
relevant GitHub issues in your commit message using GH1234 or #1234.  Either style
is fine, but the former is generally preferred:

    * a subject line with `< 80` chars.
    * One blank line.
    * Optionally, a commit message body.

Now you can commit your changes in your local repository::

    git commit -m

Combining commits
-----------------

If you have multiple commits, you may want to combine them into one commit, often
referred to as "squashing" or "rebasing".  This is a common request by package maintainers
when submitting a pull request as it maintains a more compact commit history.  To rebase
your commits::

    git rebase -i HEAD~#

Where # is the number of commits you want to combine.  Then you can pick the relevant
commit message and discard others.

To squash to the master branch do::

    git rebase -i master

Use the ``s`` option on a commit to ``squash``, meaning to keep the commit messages,
or ``f`` to ``fixup``, meaning to merge the commit messages.

Then you will need to push the branch (see below) forcefully to replace the current
commits with the new ones::

    git push origin shiny-new-feature -f


Pushing your changes
--------------------

When you want your changes to appear publicly on your GitHub page, push your
forked feature branch's commits::

    git push origin shiny-new-feature

Here ``origin`` is the default name given to your remote repository on GitHub.
You can see the remote repositories::

    git remote -v

If you added the upstream repository as described above you will see something
like::

    origin  git@github.com:yourname/pandas-gbq.git (fetch)
    origin  git@github.com:yourname/pandas-gbq.git (push)
    upstream        git://github.com/googleapis/python-bigquery-pandas.git (fetch)
    upstream        git://github.com/googleapis/python-bigquery-pandas.git (push)

Now your code is on GitHub, but it is not yet a part of the *pandas-gbq* project.  For that to
happen, a pull request needs to be submitted on GitHub.

Review your code
----------------

When you're ready to ask for a code review, file a pull request. Before you do, once
again make sure that you have followed all the guidelines outlined in this document
regarding code style, tests, performance tests, and documentation. You should also
double check your branch changes against the branch it was based on:

#. Navigate to your repository on GitHub -- https://github.com/your-user-name/pandas-gbq
#. Click on ``Branches``
#. Click on the ``Compare`` button for your feature branch
#. Select the ``base`` and ``compare`` branches, if necessary. This will be ``master`` and
   ``shiny-new-feature``, respectively.

Finally, make the pull request
------------------------------

If everything looks good, you are ready to make a pull request.  A pull request is how
code from a local repository becomes available to the GitHub community and can be looked
at and eventually merged into the master version.  This pull request and its associated
changes will eventually be committed to the master branch and available in the next
release.  To submit a pull request:

#. Navigate to your repository on GitHub
#. Click on the ``Pull Request`` button
#. You can then click on ``Commits`` and ``Files Changed`` to make sure everything looks
   okay one last time
#. Write a description of your changes in the ``Preview Discussion`` tab
#. Click ``Send Pull Request``.

This request then goes to the repository maintainers, and they will review
the code. If you need to make more changes, you can make them in
your branch, push them to GitHub, and the pull request will be automatically
updated.  Pushing them to GitHub again is done by::

    git push -f origin shiny-new-feature

This will automatically update your pull request with the latest code and restart the
Travis-CI tests.

Delete your merged branch (optional)
------------------------------------

Once your feature branch is accepted into upstream, you'll probably want to get rid of
the branch. First, merge upstream master into your branch so git knows it is safe to
delete your branch::

    git fetch upstream
    git checkout master
    git merge upstream/master

Then you can just do::

    git branch -d shiny-new-feature

Make sure you use a lower-case ``-d``, or else git won't warn you if your feature
branch has not actually been merged.

The branch will still exist on GitHub, so to delete it there do::

    git push origin --delete shiny-new-feature
