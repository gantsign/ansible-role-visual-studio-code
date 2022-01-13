Ansible Role: Visual Studio Code
================================

[![Tests](https://github.com/gantsign/ansible-role-visual-studio-code/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible-role-visual-studio-code/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.visual--studio--code-blue.svg)](https://galaxy.ansible.com/gantsign/visual-studio-code)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-visual-studio-code/master/LICENSE)

Role to install the [Visual Studio Code](https://code.visualstudio.com) IDE / text editor.

Requirements
------------

* Ansible >= 2.8

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)

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
# if yes
# - for apt repo the option trusted=yes is NOT added
# - for dnf/yum the option gpgcheck is set to yes
# - for zypper the option gpgcheck is set to 1
# yes is the default
# if no
# - for apt repo the option trusted=yes is added to repo definition
# - for dnf/yum the option gpgcheck is set to no
# - for zypper the option gpgcheck is set to 0
visual_studio_code_gpgcheck: yes

# skip task to add repo for remote package manager
# if set to yes, the task 'install VS Code repo (apt/yum/dnf/zypper)' will be skipped
# if set to no, the repo will be added, this is the default
visual_studio_code_skip_add_repo: no

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
    visual_studio_code_settings_overwrite: # Overwrite the settings file if it exists. Options: boolean "yes" or "no" (defaults to "no").
    visual_studio_code_settings: # JSON object
```

Example Playbooks
-----------------

Minimal playbook:

```yaml
- hosts: servers
  roles:
    - role: gantsign.visual-studio-code
```

Playbook with extensions installed that overwrites settings:

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
          visual_studio_code_settings_overwrite: yes
          visual_studio_code_settings: {
            "editor.rulers": [80, 100, 120],
            "editor.renderWhitespace": true,
            "files.associations": {
              "Vagrantfile": "ruby"
            }
          }
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
