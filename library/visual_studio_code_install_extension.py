#!/usr/bin/python

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

import os

from ansible.module_utils.basic import AnsibleModule

__metaclass__ = type


def is_extension_installed(module, name):
    rc, out, err = module.run_command(['code', '--list-extensions', name])
    if rc != 0 or err:
        module.fail_json(
            msg='Error querying installed extensions [%s]: %s' % (name,
                                                                  out + err))
    lowername = name.lower()
    match = next((x for x in out.splitlines() if x.lower() == lowername), None)
    return match is not None


def install_extension(module, name):
    if is_extension_installed(module, name):
        return False
    else:
        rc, out, err = module.run_command(
            ['code', '--install-extension', name])
        if rc != 0 or err:
            module.fail_json(
                msg='Error while installing extension [%s]: %s' % (name,
                                                                   out + err))
        return not 'already installed' in out


def run_module():

    module_args = dict(
        name=dict(type='str', required=True))

    module = AnsibleModule(argument_spec=module_args,
                           supports_check_mode=False)

    name = module.params['name']

    changed = install_extension(module, name)

    if changed:
        msg = '%s is now installed' % name
    else:
        msg = '%s is already installed' % name

    module.exit_json(changed=changed, msg=msg)


def main():
    run_module()


if __name__ == '__main__':
    main()
