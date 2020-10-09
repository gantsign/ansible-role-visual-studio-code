#!/usr/bin/python

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

import os

from ansible.module_utils.basic import AnsibleModule

__metaclass__ = type


def is_extension_installed(module, executable, name):
    rc, out, err = module.run_command([executable, '--list-extensions', name])
    if rc != 0 or err:
        module.fail_json(
            msg='Error querying installed extensions [%s]: %s' % (name,
                                                                  out + err))
    lowername = name.lower()
    match = next((x for x in out.splitlines() if x.lower() == lowername), None)
    return match is not None


def list_extension_dirs(module, executable):
    dirname = '.vscode'
    if executable == 'code-insiders':
        dirname += '-insiders'

    ext_dir = os.path.expanduser(
        os.path.join('~', dirname, 'extensions'))

    ext_dirs = sorted([f for f in os.listdir(
        ext_dir) if os.path.isdir(os.path.join(ext_dir, f))])
    return ext_dirs


def install_extension(module, executable, name):
    if is_extension_installed(module, executable, name):
        # Use the fact that extension directories names contain the version
        # number
        before_ext_dirs = list_extension_dirs(module, executable)
        # Unfortunately `--force` suppresses errors (such as extension not
        # found)
        rc, out, err = module.run_command(
            [executable, '--install-extension', name, '--force'])
        # Whitelist: [DEP0005] DeprecationWarning: Buffer() is deprecated due
        # to security and usability issues.
        if rc != 0 or (err and '[DEP0005]' not in err):
            module.fail_json(
                msg='Error while upgrading extension [%s]: (%d) %s' %
                (name, rc, out + err))
        after_ext_dirs = list_extension_dirs(module, executable)
        changed = before_ext_dirs != after_ext_dirs
        return changed, 'upgrade'
    else:
        rc, out, err = module.run_command(
            [executable, '--install-extension', name])
        # Whitelist: [DEP0005] DeprecationWarning: Buffer() is deprecated due
        # to security and usability issues.
        if rc != 0 or (err and '[DEP0005]' not in err):
            module.fail_json(
                msg='Error while installing extension [%s]: (%d) %s' %
                (name, rc, out + err))
        changed = 'already installed' not in out
        return changed, 'install'


def run_module():

    module_args = dict(
        executable=dict(
            type='str',
            required=False,
            choices=[
                'code',
                'code-insiders'],
            default='code'),
        name=dict(
            type='str',
            required=True))

    module = AnsibleModule(argument_spec=module_args,
                           supports_check_mode=False)

    executable = module.params['executable']
    if executable != 'code-insiders':
        executable = 'code'

    name = module.params['name']

    changed, change = install_extension(module, executable, name)

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
