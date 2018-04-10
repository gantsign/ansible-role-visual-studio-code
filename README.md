Ansible Role: Visual Studio Code
================================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-visual-studio-code.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-visual-studio-code)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.visual--studio--code-blue.svg)](https://galaxy.ansible.com/gantsign/visual-studio-code)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-visual-studio-code/master/LICENSE)

Role to install the [Visual Studio Code](https://code.visualstudio.com) IDE / text editor.

Requirements
------------

* Ansible >= 2.3 (earlier versions may work but are not tested)
* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Visual Studio Code version number (defaults to the latest version)
visual_studio_code_version: ''

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

Playbook with extensions installed:

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

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
