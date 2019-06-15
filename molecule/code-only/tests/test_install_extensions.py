import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('extension', [
    'ms-python.python',
    'wholroyd.jinja'
])
def test_visual_studio_code(host, extension):
    output = host.check_output('sudo --user test_usr -H code %s %s',
                               '--install-extension', extension)
    assert 'already installed' in output
