Ansible Role: Visual Studio Code
================================

[![Tests](https://github.com/gantsign/ansible-role-visual-studio-code/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible-role-visual-studio-code/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.visual--studio--code-blue.svg)](https://galaxy.ansible.com/gantsign/visual-studio-code)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-visual-studio-code/master/LICENSE)

Role to install the [Visual Studio Code](https://code.visualstudio.com) IDE / text editor.

Requirements
------------

* Ansible Core >= 2.12

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)
            * Jammy (22.04)

    * RedHat Family

        * Rocky Linux

            * 8

        * Fedora

            * 35

    * SUSE Family

        * openSUSE

            * 15.3

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Visual Studio Code version number (defaults to the latest version)
visual_studio_code_version: ''

# Build (either 'stable' or 'insiders') https://code.visualstudio.com/insiders/
# Ubuntu only (code-insiders isn't in Microsoft's RPM repo)
visual_studio_code_build: stable

# Mirror server for fetching the public keys and the Visual Studio Code
# installation package. The URL may include directories. The URL must not end
# with a trailing slash.
visual_studio_code_mirror: 'https://packages.microsoft.com'

# should the gpgcheck of the repo enabled?
# if true
# - for apt repo the option trusted=yes is NOT added
# - for dnf/yum the option gpgcheck is set to yes
# - for zypper the option gpgcheck is set to 1
# true is the default
# if false
# - for apt repo the option trusted=yes is added to repo definition
# - for dnf/yum the option gpgcheck is set to no
# - for zypper the option gpgcheck is set to 0
visual_studio_code_gpgcheck: true

# skip task to add repo for remote package manager
# if set to true, the task 'install VS Code repo (apt/yum/dnf/zypper)' will be skipped
# if set to false, the repo will be added, this is the default
visual_studio_code_skip_add_repo: false

# Users to install extensions for and/or write settings.json
users: []
```

Users are configured as follows:

```yaml
users:
  - username: # Unix user name
    visual_studio_code_extensions:
      - # extension 1
      - # extension 2
    visual_studio_code_settings_overwrite: # Overwrite the settings file if it exists. Options: boolean "true" or "false" (defaults to "false").
    visual_studio_code_settings: # JSON object
    visual_studio_code_keybindings_overwrite: # Overwrite the keybindings file if it exists. Options: boolean "true" or "false" (defaults to "false").
    visual_studio_code_keybindings: # JSON array
```

Example Playbooks
-----------------

Minimal playbook:

```yaml
- hosts: servers
  roles:
    - role: gantsign.visual-studio-code
```

Playbook with extensions installed that overwrites settings and keybindings:

```yaml
- hosts: servers
  roles:
    - role: gantsign.visual-studio-code
      users:
        - username: vagrant
          visual_studio_code_extensions:
            - streetsidesoftware.code-spell-checker
            - wholroyd.jinja
            - ms-python.python
          visual_studio_code_settings_overwrite: true
          visual_studio_code_settings: {
            "editor.rulers": [80, 100, 120],
            "editor.renderWhitespace": true,
            "files.associations": {
              "Vagrantfile": "ruby"
            }
          }
          visual_studio_code_keybindings_overwrite: true
          visual_studio_code_keybindings: [
            {
              "key":     "ctrl+'",
              "command": "workbench.action.terminal.focus"
            },
            {
              "key":     "ctrl+'",
              "command": "workbench.action.focusActiveEditorGroup",
              "when":    "terminalFocus"
            }
          ]
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses the following tooling:
* [Molecule](http://molecule.readthedocs.io/) for orchestrating test scenarios
* [Testinfra](http://testinfra.readthedocs.io/) for testing the changes on the
  remote
* [pytest](http://docs.pytest.org/) the testing framework
* [Tox](https://tox.wiki/en/latest/) manages Python virtual
  environments for linting and testing
* [pip-tools](https://github.com/jazzband/pip-tools) for managing dependencies

A Visual Studio Code
[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) is
provided for developing and testing this role.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
