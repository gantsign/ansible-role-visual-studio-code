Ansible Role: Visual Studio Code
================================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-visual-studio-code.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-visual-studio-code)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.visual--studio--code-blue.svg)](https://galaxy.ansible.com/gantsign/visual-studio-code)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-visual-studio-code/master/LICENSE)

Role to install the [Visual Studio Code](https://code.visualstudio.com) IDE / text editor.

Requirements
------------

* Ansible >= 2.0
* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Visual Studio Code version number
visual_studio_code_version: '1.14.2'

# Directory to store files downloaded for Visual Studio Code installation
visual_studio_code_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"

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

### Supported Visual Studio Code Versions

The following versions of Visual Studio Code are supported without any
additional configuration (for other versions follow the Advanced Configuration
instructions):

* `1.14.2`
* `1.14.1`
* `1.14`
* `1.13.1`
* `1.13`
* `1.12.2`
* `1.12.1`
* `1.12`
* `1.11.2`
* `1.11.1`
* `1.11`
* `1.10.2`
* `1.10.1`
* `1.10`
* `1.9.1`
* `1.9`
* `1.8.1`
* `1.8`
* `1.7.2`
* `1.7.1`
* `1.7`
* `1.6.1`
* `1.6`
* `1.5.3`
* `1.5.2`
* `1.5.1`
* `1.5`
* `1.4`
* `1.3.1`
* `1.3`

Advanced Configuration
----------------------

The following role variables are dependent on the Visual Studio Code version;
to use a Visual Studio Code version **not pre-configured by this role** you
must configure the variables below:

```yaml
# SHA256 sum for the redistributable package (e.g code_1.3.0-1467909982_amd64.deb)
visual_studio_code_redis_sha256sum: '53eb2cd235b395a28e7fda6f50f904fd5665877e354609f836a6b60a1592c9c9'

# The download URL for the redistributable package
# Permanent download URLs can be found on https://code.visualstudio.com/Updates
visual_studio_code_redis_url: 'https://az764295.vo.msecnd.net/stable/e724f269ded347b49fcf1657fc576399354e6703/code_1.3.0-1467909982_amd64.deb'
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
            - donjayamanne.python
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
