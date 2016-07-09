Ansible Role: Visual Studio Code
================================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-visual-studio-code.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-visual-studio-code)

Role to install the [Visual Studio Code](https://code.visualstudio.com) IDE / text editor.

Requirements
------------

* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Visual Studio Code version number
visual_studio_code_version: 1.3

# Path for Ansible to store downloaded files
local_ansible_data_path: '/tmp/ansible/data'

# SHA256 sum for the redistributable package
visual_studio_code_redis_sha256sum: 53eb2cd235b395a28e7fda6f50f904fd5665877e354609f836a6b60a1592c9c9

# The download URL for the redistributable package
visual_studio_code_redis_url: https://az764295.vo.msecnd.net/stable/e724f269ded347b49fcf1657fc576399354e6703/code_1.3.0-1467909982_amd64.deb
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - { role: gantsign.visual-studio-code }
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
