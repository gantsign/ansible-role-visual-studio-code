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


def list_extension_dirs(module):
    ext_dir = os.path.expanduser(
        os.path.join('~', '.vscode', 'extensions'))

    ext_dirs = [f for f in os.listdir(
        ext_dir) if os.path.isdir(os.path.join(ext_dir, f))]
    ext_dirs.sort()
    return ext_dirs


def install_extension(module, name):
    if is_extension_installed(module, name):
        # Use the fact that extension directories names contain the version number
        before_ext_dirs = list_extension_dirs(module)
        # Unfortunately `--force` suppresses errors (such as extension not found)
        rc, out, err = module.run_command(
            ['code', '--install-extension', name, '--force'])
        # Whitelist: [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues.
        if rc != 0 or (err and '[DEP0005]' not in err):
            module.fail_json(
                msg='Error while upgrading extension [%s]: (%d) %s' % (name,
                                                                       rc,
                                                                       out + err))
        after_ext_dirs = list_extension_dirs(module)
        changed = before_ext_dirs != after_ext_dirs
        return changed, 'upgrade'
    else:
        rc, out, err = module.run_command(
            ['code', '--install-extension', name])
        # Whitelist: [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues.
        if rc != 0 or (err and '[DEP0005]' not in err):
            module.fail_json(
                msg='Error while installing extension [%s]: (%d) %s' % (name,
                                                                        rc,
                                                                        out + err))
        changed = not 'already installed' in out
        return changed, 'install'


def run_module():

    module_args = dict(
        name=dict(type='str', required=True))

    module = AnsibleModule(argument_spec=module_args,
                           supports_check_mode=False)

    name = module.params['name']

    changed, change = install_extension(module, name)

    if changed:
        if change == 'upgrade':
            msg = '%s was upgraded' % name
        else:
            msg = '%s is now installed' % name
    else:
        msg = '%s is already installed' % name

    module.exit_json(changed=changed, msg=msg)


def main():
    run_module()


if __name__ == '__main__':
    main()
