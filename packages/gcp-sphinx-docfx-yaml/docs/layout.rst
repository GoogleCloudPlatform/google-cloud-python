Layout of the project
=====================

This project has a couple components:

* This repo, which houses the YAML conversion code:
   * https://github.com/ericholscher/sphinx-docfx-yaml/
* There is a Travis CI build that tests the actual Python YAML generation code on Python 2 & 3:
   * https://github.com/ericholscher/sphinx-docfx-yaml/blob/master/.travis.yml
* The Appveyor CI build that works as an integration test for the Python SDK library:
   * https://github.com/ericholscher/sphinx-docfx-yaml/blob/master/appveyor.yml
* The HTML output of the CI build, which does a full life cycle Sphinx->YAML->Docfx conversion:
   * https://ci.appveyor.com/project/ericholscher/sphinx-docfx-yaml/build/artifacts
   * The YAML is in the ``doc/_build/html/docfx_yaml`` directory
   * The rendered HTML is in the ``doc/_site/api/html/docfx_yaml`` directory
   * The generated YAML is also checked into GitHub here: https://github.com/bradygaster/python-sdk-dev/tree/eric-full-yaml-test/python-sdk-dev/docfx_yaml
* A forked version of the Python SDK that adds integrates the YAML output and the docfx configuration:
   * https://github.com/Azure/azure-sdk-for-python/compare/master...ericholscher:add-docfx-yaml
   * This is used in the CI steps above to make sure we properly generate the YAML & docfx docs
