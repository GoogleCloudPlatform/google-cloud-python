# Copyright 2016 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Shared helper functions for RuntimeConfig API classes."""


def config_name_from_full_name(full_name):
    """Extract the config name from a full resource name.

      >>> config_name_from_full_name('projects/my-proj/configs/my-config')
      "my-config"

    :type full_name: str
    :param full_name:
        The full resource name of a config. The full resource name looks like
        ``projects/project-name/configs/config-name`` and is returned as the
        ``name`` field of a config resource.  See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs

    :rtype: str
    :returns: The config's short name, given its full resource name.
    :raises: :class:`ValueError` if ``full_name`` is not the expected format
    """
    projects, _, configs, result = full_name.split("/")
    if projects != "projects" or configs != "configs":
        raise ValueError(
            "Unexpected format of resource",
            full_name,
            'Expected "projects/{proj}/configs/{cfg}"',
        )
    return result


def variable_name_from_full_name(full_name):
    """Extract the variable name from a full resource name.

      >>> variable_name_from_full_name(
              'projects/my-proj/configs/my-config/variables/var-name')
      "var-name"
      >>> variable_name_from_full_name(
              'projects/my-proj/configs/my-config/variables/another/var/name')
      "another/var/name"

    :type full_name: str
    :param full_name:
        The full resource name of a variable. The full resource name looks like
        ``projects/prj-name/configs/cfg-name/variables/var-name`` and is
        returned as the ``name`` field of a variable resource.  See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables

    :rtype: str
    :returns: The variable's short name, given its full resource name.
    :raises: :class:`ValueError` if ``full_name`` is not the expected format
    """
    projects, _, configs, _, variables, result = full_name.split("/", 5)
    if projects != "projects" or configs != "configs" or variables != "variables":
        raise ValueError(
            "Unexpected format of resource",
            full_name,
            'Expected "projects/{proj}/configs/{cfg}/variables/..."',
        )
    return result
